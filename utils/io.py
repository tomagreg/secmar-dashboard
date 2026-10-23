"""Download, local cache and loading of SECMAR data."""

from pathlib import Path

import pandas as pd
import requests

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

SOURCE_URLS = {
    "operations.csv": "https://secmar.antoine-augusti.fr/operations.csv",
    "operations_stats.csv": "https://secmar.antoine-augusti.fr/operations_stats.csv",
}

DATASET_PAGE = "https://www.data.gouv.fr/datasets/operations-coordonnees-par-les-cross"
DOC_URL = "https://mtes-mct.github.io/secmar-documentation/"

OPERATIONS_COLS = [
    "operation_id", "cross", "est_metropolitain", "evenement", "categorie_evenement",
    "latitude", "longitude", "vent_force", "mer_force",
    "date_heure_reception_alerte", "date_heure_fin_operation",
]
STATS_COLS = [
    "operation_id", "annee", "mois", "distance_cote_milles_nautiques",
    "nombre_personnes_impliquees", "nombre_personnes_tous_deces_ou_disparues",
]


def fetch_and_cache(filename: str) -> Path:
    """Return the local path of a data file, downloading it if missing."""
    path = DATA_DIR / filename
    if path.exists():
        return path
    DATA_DIR.mkdir(exist_ok=True)
    with requests.get(SOURCE_URLS[filename], stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 20):
                f.write(chunk)
    return path


def load_data() -> pd.DataFrame:
    """Load operations joined with their statistics, one row per operation."""
    ops = pd.read_csv(fetch_and_cache("operations.csv"), usecols=OPERATIONS_COLS)
    stats = pd.read_csv(fetch_and_cache("operations_stats.csv"), usecols=STATS_COLS)
    return ops.merge(stats, on="operation_id", how="left", validate="one_to_one")


if __name__ == "__main__":
    for name in SOURCE_URLS:
        print(fetch_and_cache(name))
