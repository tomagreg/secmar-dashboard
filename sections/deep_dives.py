"""Section 3: frequency vs severity, conditions, map."""

import pandas as pd
import streamlit as st

from utils.i18n import t
from utils.prep import MIN_OPS_MOTIF
from utils.viz import bar_chart, grouped_bar_chart, line_chart, map_chart, show

TOP_N = 10


def render_frequence_gravite(tables: dict[str, pd.DataFrame], ref: float) -> None:
    """Act A: share of operations vs share of deaths, and deadliest reasons."""
    st.subheader(t("a_sub"))
    show(grouped_bar_chart(
        tables["by_categorie"], "categorie_evenement", ["part_operations", "part_deces"],
        [t("share_ops"), t("share_deaths")], t("axis_share"), t("axis_category")),
        t("read_a1"))

    top = tables["by_motif"].nlargest(TOP_N, "letalite")
    show(bar_chart(
        top, "letalite", "evenement", t("axis_lethal"), t("axis_motif"),
        horizontal=True, ref_value=ref, ref_label=t("mean", v=ref)),
        t("read_a2", n=MIN_OPS_MOTIF), text_first=True)


def render_conditions(tables: dict[str, pd.DataFrame], ref: float) -> None:
    """share of fatal operations by wind, sea state and distance to the coast."""
    st.subheader(t("b_sub"))
    meteo = pd.concat([
        tables["by_vent"].rename(columns={"vent_force": "force"}).assign(serie=t("axis_wind")),
        tables["by_mer"].rename(columns={"mer_force": "force"}).assign(serie=t("axis_sea")),
    ])
    fig = line_chart(meteo, "force", "letalite", t("axis_force"), t("axis_lethal"), color="serie")
    fig.add_hline(y=ref, line_dash="dash", annotation_text=t("mean", v=ref))
    show(fig, t("read_b1"))

    show(bar_chart(
        tables["by_distance"], "tranche_distance", "letalite",
        t("axis_distance"), t("axis_lethal"), ref_value=ref, ref_label=t("mean", v=ref)),
        t("read_b2"), text_first=True)


def render_map(tables: dict[str, pd.DataFrame], map_var: str) -> None:
    """map by grid cell and CROSS ranking."""
    st.subheader(t("c_sub"))
    labels = {"operations": t("kpi_ops"), "letalite": t("axis_lethal")}
    show(map_chart(tables["geo"], map_var, labels), t("read_map"))

    show(bar_chart(
        tables["by_cross"], "operations", "cross", t("axis_ops"), t("axis_cross"),
        horizontal=True), t("read_cross"), text_first=True)


def render(tables: dict[str, pd.DataFrame], k: dict, map_var: str) -> None:
    """Render the three deep-dive acts."""
    st.header(t("dd_header"))
    ref = k["letalite_hors_corps"]
    render_frequence_gravite(tables, ref)
    render_conditions(tables, ref)
    render_map(tables, map_var)
