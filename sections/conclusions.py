"""Section 4: data quality, takeaways and next steps."""

import streamlit as st

from utils.i18n import fmt_int, t


def render_quality(q: dict) -> None:
    """Render missing values, duplicates and validation checks."""
    st.header(t("q_header"))
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(t("q_dup_ids"), q["doublons_id"])
    c2.metric(t("q_dup_rows"), q["lignes_dupliquees"])
    c3.metric(t("q_neg"), q["durees_negatives"], help=t("q_neg_help"))
    c4.metric(t("q_coords"), q["coordonnees_invalides"], help=t("q_coords_help"))
    st.markdown(t("q_period", start=q["annees"][0], end=q["annees"][1],
                  rows=fmt_int(q["lignes"]), bodies=fmt_int(q["decouvertes_corps"])))
    st.markdown(t("q_land", pct=q["distance_nulle_pct"]))
    with st.expander(t("q_missing")):
        st.dataframe(q["manquants"].rename(t("q_missing_col")))
    st.info(t("q_bias"))


def render() -> None:
    """Render the key messages, implications and next steps."""
    st.header(t("c_header"))
    st.success(t("c_messages"))
    st.markdown(t("c_next"))
