"""Section 2: KPI header and high-level trends."""

import pandas as pd
import streamlit as st

from utils.i18n import fmt_int, t
from utils.viz import bar_chart, line_chart, show


def render_kpis(k: dict) -> None:
    """Render the five KPIs computed on filtered operations."""
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric(t("kpi_ops"), fmt_int(k["operations"]))
    c2.metric(t("kpi_people"), fmt_int(k["personnes"]))
    c3.metric(t("kpi_deaths"), fmt_int(k["morts_disparus"]))
    c4.metric(t("kpi_lethal"), f"{k['letalite']:.1f} %", help=t("kpi_lethal_help"))
    c5.metric(t("kpi_duration"), f"{k['duree_mediane']:.1f} h", help=t("kpi_duration_help"))


def render(k: dict, tables: dict[str, pd.DataFrame], incomplete_year: int) -> None:
    """Render the KPIs, yearly trend and seasonality."""
    st.header(t("overview_header"))
    render_kpis(k)
    st.caption(t("read_note"))

    st.subheader(t("ops_year"))
    fig = line_chart(tables["timeseries"], "annee", "operations", t("axis_year"), t("axis_ops"))
    if incomplete_year in tables["timeseries"]["annee"].values:
        fig.add_vline(x=incomplete_year, line_dash="dot",
                      annotation_text=t("incomplete", year=incomplete_year))
    show(fig, t("read_year"))

    st.subheader(t("ops_month"))
    months = t("months")
    by_month = tables["by_month"].assign(mois_nom=lambda d: d["mois"].map(lambda m: months[m - 1]))
    show(bar_chart(by_month, "mois_nom", "operations", t("axis_month"), t("axis_ops")),
         t("read_month"), text_first=True)
