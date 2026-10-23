"""Streamlit entry point: cached loading, sidebar, sections."""

from pathlib import Path

import pandas as pd
import streamlit as st

from sections import conclusions, deep_dives, intro, overview
from utils.i18n import t
from utils.io import DATASET_PAGE, DOC_URL, load_data
from utils.prep import clean, filter_data, kpis, make_tables, quality_report
from utils.viz import CSS

st.set_page_config(page_title="SECMAR — CROSS", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

LOGO_PATH = Path(__file__).resolve().parent / "assets" / "logo.png"


@st.cache_resource(show_spinner="Loading SECMAR data…")
def get_data() -> tuple[pd.DataFrame, dict]:
    """Load, clean and check the data once for the whole app."""
    raw = load_data()
    return clean(raw), quality_report(raw)


@st.cache_data(show_spinner=False)
def get_tables(years: tuple[int, int], crosses: list[str], categories: list[str],
               zone: str) -> tuple[dict, dict[str, pd.DataFrame]]:
    """Filter operations and compute KPIs and aggregated tables, cached per filter set."""
    df, _ = get_data()
    sub = filter_data(df, years, crosses, categories, zone)
    return kpis(sub), make_tables(sub)


def render_about() -> None:
    """Render the author and project information as a card above the title."""
    with st.container(key="card-about"):
        logo_col, author_col, course_col = st.columns([1, 2, 2], vertical_alignment="center")
        with logo_col.container(key="logo"):
            st.image(str(LOGO_PATH))
        author_col.markdown(
            f"#### {t('about')}\n\n"
            "**Thomas GREGOIRE** · I2-BIO · 2026  \n"
            "tomagreg2@gmail.com  \n"
            "[GitHub](https://github.com/tomagreg/) · "
            "[LinkedIn](https://www.linkedin.com/in/thomas-gregoire-3b5925251)"
        )
        course_col.markdown(
            f"*{t('about_course')}*  \n"
            f"{t('about_prof')}  \n"
            "mano.mathew@efrei.fr"
        )


df, quality = get_data()
year_min, year_max = int(df["annee"].min()), int(df["annee"].max())

with st.sidebar:
    st.radio("Langue / Language", ["fr", "en"], key="lang", horizontal=True,
             format_func={"fr": "Français", "en": "English"}.get)
    st.header(t("filters"))
    with st.container(border=True):
        years = st.slider(t("period"), year_min, year_max, (year_min, year_max - 1),
                          help=t("period_help", year=year_max), key="years")
        zone = st.radio(t("zone"), ["all", "metro", "overseas"],
                        format_func=lambda z: t(f"zone_{z}"), key="zone")
        crosses = st.multiselect(t("cross"), sorted(df["cross"].dropna().unique()),
                                 placeholder=t("all_m"), key="crosses")
        categories = st.multiselect(t("category"),
                                    sorted(df["categorie_evenement"].dropna().unique()),
                                    placeholder=t("all_f"), key="categories")
        map_var = st.selectbox(t("map_var"), ["operations", "letalite"],
                               format_func=lambda v: t(f"var_{v}"), key="map_var")

render_about()
st.title(t("title"))
st.caption(f"{t('license')} [{t('dataset')}]({DATASET_PAGE}) · [{t('doc')}]({DOC_URL})")

k, tables = get_tables(years, crosses, categories, zone)

intro.render()
if k["operations"] == 0:
    st.warning(t("no_data"))
    st.stop()
overview.render(k, tables, incomplete_year=year_max)
deep_dives.render(tables, k, map_var)
conclusions.render_quality(quality)
conclusions.render()
