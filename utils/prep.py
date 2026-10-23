"""Cleaning, quality checks, filtering and pre-aggregated tables."""

import pandas as pd

DECOUVERTE_CORPS = "Découverte de corps"
DISTANCE_BINS = [0, 0.5, 2, 10, 50, float("inf")]
DISTANCE_LABELS = ["< 0.5", "0.5 – 2", "2 – 10", "10 – 50", "> 50"]
MAP_GRID_DEG = 0.05
MIN_OPS_MOTIF = 200


def invalid_coords(df: pd.DataFrame) -> pd.Series:
    """Flag coordinates out of bounds or set to placeholder values (0, 0), -90 or -180."""
    lat, lon = df["latitude"], df["longitude"]
    hors_bornes = ~lat.between(-90, 90) | ~lon.between(-180, 180)
    factices = ((lat == 0) & (lon == 0)) | (lat == -90) | (lon == -180)
    return lat.notna() & lon.notna() & (hors_bornes | factices)


def clean(raw: pd.DataFrame) -> pd.DataFrame:
    """Clean the raw table and add derived columns."""
    df = raw.copy()
    debut = pd.to_datetime(df["date_heure_reception_alerte"], utc=True, errors="coerce")
    fin = pd.to_datetime(df["date_heure_fin_operation"], utc=True, errors="coerce")
    duree = (fin - debut).dt.total_seconds() / 3600
    df["duree_h"] = duree.where(duree >= 0)
    df["morts_disparus"] = df["nombre_personnes_tous_deces_ou_disparues"].fillna(0)
    df["mortelle"] = df["morts_disparus"] > 0
    df["decouverte_corps"] = df["evenement"] == DECOUVERTE_CORPS
    df["tranche_distance"] = pd.cut(df["distance_cote_milles_nautiques"], DISTANCE_BINS,
                                    labels=DISTANCE_LABELS, right=False)
    df.loc[invalid_coords(df), ["latitude", "longitude"]] = None
    return df


def quality_report(raw: pd.DataFrame) -> dict:
    """Compute data quality checks on the raw table."""
    debut = pd.to_datetime(raw["date_heure_reception_alerte"], utc=True, errors="coerce")
    fin = pd.to_datetime(raw["date_heure_fin_operation"], utc=True, errors="coerce")
    return {
        "lignes": len(raw),
        "manquants": (raw.isna().mean() * 100).round(1).sort_values(ascending=False),
        "doublons_id": int(raw["operation_id"].duplicated().sum()),
        "lignes_dupliquees": int(raw.duplicated().sum()),
        "durees_negatives": int(((fin - debut).dt.total_seconds() < 0).sum()),
        "coordonnees_invalides": int(invalid_coords(raw).sum()),
        "distance_nulle_pct": (raw["distance_cote_milles_nautiques"].dropna() == 0).mean() * 100,
        "decouvertes_corps": int((raw["evenement"] == DECOUVERTE_CORPS).sum()),
        "annees": (int(raw["annee"].min()), int(raw["annee"].max())),
    }


def filter_data(df: pd.DataFrame, years: tuple[int, int], crosses: list[str],
                categories: list[str], zone: str) -> pd.DataFrame:
    """Apply the sidebar filters."""
    mask = df["annee"].between(*years)
    if crosses:
        mask &= df["cross"].isin(crosses)
    if categories:
        mask &= df["categorie_evenement"].isin(categories)
    if zone != "all":
        mask &= df["est_metropolitain"] == (zone == "metro")
    return df[mask]


def _letalite(g: pd.core.groupby.DataFrameGroupBy) -> pd.DataFrame:
    """Aggregate a groupby into operations, dead/missing and share of fatal operations."""
    out = g.agg(operations=("operation_id", "size"),
                morts_disparus=("morts_disparus", "sum"),
                mortelles=("mortelle", "sum"))
    out["letalite"] = out["mortelles"] / out["operations"] * 100
    return out.reset_index()


def kpis(df: pd.DataFrame) -> dict:
    """Compute the KPI header values."""
    n = len(df)
    hors_corps = df.loc[~df["decouverte_corps"], "mortelle"]
    return {
        "operations": n,
        "personnes": int(df["nombre_personnes_impliquees"].sum()),
        "morts_disparus": int(df["morts_disparus"].sum()),
        "letalite": df["mortelle"].mean() * 100 if n else 0.0,
        "letalite_hors_corps": hors_corps.mean() * 100 if len(hors_corps) else 0.0,
        "duree_mediane": df["duree_h"].median() if n else float("nan"),
    }


def make_tables(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Build the pre-aggregated tables used by the charts."""
    hors_corps = df[~df["decouverte_corps"]]

    by_cat = _letalite(df.groupby("categorie_evenement"))
    by_cat["part_operations"] = by_cat["operations"] / by_cat["operations"].sum() * 100
    by_cat["part_deces"] = by_cat["morts_disparus"] / max(by_cat["morts_disparus"].sum(), 1) * 100
    by_cat = by_cat.sort_values("part_deces", ascending=False)

    by_motif = _letalite(hors_corps.groupby("evenement"))
    by_motif = by_motif[by_motif["operations"] >= MIN_OPS_MOTIF]

    geo = hors_corps.dropna(subset=["latitude", "longitude"]).copy()
    geo["latitude"] = (geo["latitude"] / MAP_GRID_DEG).round() * MAP_GRID_DEG
    geo["longitude"] = (geo["longitude"] / MAP_GRID_DEG).round() * MAP_GRID_DEG

    return {
        "timeseries": _letalite(df.groupby("annee")),
        "by_month": _letalite(df.groupby("mois")),
        "by_categorie": by_cat,
        "by_motif": by_motif,
        "by_mer": _letalite(hors_corps.groupby("mer_force")),
        "by_vent": _letalite(hors_corps.groupby("vent_force")),
        "by_distance": _letalite(hors_corps.groupby("tranche_distance", observed=False)),
        "by_cross": _letalite(df.groupby("cross")).sort_values("operations", ascending=False),
        "geo": _letalite(geo.groupby(["latitude", "longitude"])),
    }
