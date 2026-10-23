"""Plotly chart functions and page styling shared by all sections."""

import hashlib

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

NAVY = "#003362"
CARD_BLUE = "#174e85"
YELLOW = "#ffd139"
ORANGE = "#ffa040"
WHITE = "#ffffff"

CSS = f"""
<style>
.stApp h1, .stApp h2, .stApp h3, .stApp h4 {{ color: {ORANGE}; }}
.stApp strong, .stApp b {{ color: {ORANGE}; }}
[class*="st-key-card-"] {{
    background: {CARD_BLUE}; border: 1px solid {ORANGE}; border-radius: 12px; padding: 1rem;
}}
[class*="st-key-logo"] {{ background: {WHITE}; border-radius: 8px; padding: 8px; }}
</style>
"""

pio.templates["snsm"] = go.layout.Template(
    layout=dict(
        colorway=[YELLOW, WHITE], font=dict(color=WHITE),
        paper_bgcolor=CARD_BLUE, plot_bgcolor=CARD_BLUE,
        xaxis=dict(gridcolor="rgba(255,255,255,0.15)", zerolinecolor="rgba(255,255,255,0.3)"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.15)", zerolinecolor="rgba(255,255,255,0.3)"),
    ),
    data=dict(
        bar=[go.Bar(marker_line_color=NAVY, marker_line_width=1)],
        scatter=[go.Scatter(line_width=3, marker=dict(size=8, line=dict(color=NAVY, width=1)))],
    ),
)
pio.templates.default = "plotly_dark+snsm"


def show(fig: go.Figure, text: str, text_first: bool = False) -> None:
    """Render a chart and its interpretation side by side in a card."""
    key = "card-" + hashlib.md5(text.encode()).hexdigest()[:8]
    fig.update_layout(paper_bgcolor=CARD_BLUE, plot_bgcolor=CARD_BLUE)
    with st.container(key=key):
        if text_first:
            text_col, chart_col = st.columns([1, 2], vertical_alignment="center")
        else:
            chart_col, text_col = st.columns([2, 1], vertical_alignment="center")
        chart_col.plotly_chart(fig, theme=None)
        text_col.markdown(text)


def line_chart(df: pd.DataFrame, x: str, y: str, x_title: str, y_title: str,
               color: str | None = None) -> go.Figure:
    """Line chart of one series, or one line per value of color."""
    return px.line(df, x=x, y=y, color=color, markers=True,
                   labels={x: x_title, y: y_title, color: ""} if color else {x: x_title, y: y_title})


def bar_chart(
    df: pd.DataFrame, x: str, y: str, x_title: str, y_title: str,
    horizontal: bool = False, ref_value: float | None = None, ref_label: str = "",
) -> go.Figure:
    """Bar chart of a single series, with an optional dashed reference line."""
    fig = px.bar(df, x=x, y=y, orientation="h" if horizontal else "v",
                 labels={x: x_title, y: y_title})
    if ref_value is not None:
        if horizontal:
            fig.add_vline(x=ref_value, line_dash="dash", annotation_text=ref_label)
        else:
            fig.add_hline(y=ref_value, line_dash="dash", annotation_text=ref_label)
    if horizontal:
        fig.update_yaxes(categoryorder="total ascending")
    return fig


def grouped_bar_chart(
    df: pd.DataFrame, category: str, values: list[str], labels: list[str],
    x_title: str, y_title: str,
) -> go.Figure:
    """Horizontal grouped bars comparing several measures per category."""
    long = df.rename(columns=dict(zip(values, labels))).melt(
        id_vars=category, value_vars=labels, var_name=" ", value_name="valeur"
    )
    fig = px.bar(long, x="valeur", y=category, color=" ", barmode="group",
                 orientation="h", labels={"valeur": x_title, category: y_title})
    fig.update_yaxes(categoryorder="array", categoryarray=df[category].tolist()[::-1])
    return fig


def map_chart(df: pd.DataFrame, value: str, labels: dict[str, str]) -> go.Figure:
    """Map of operations aggregated by grid cell."""
    return px.scatter_map(
        df, lat="latitude", lon="longitude", size="operations", color=value,
        color_continuous_scale=px.colors.sequential.Oranges[3:], size_max=15, zoom=4.3,
        center={"lat": 46.5, "lon": -1.5}, map_style="open-street-map", height=600,
        labels=labels,
        hover_data={"operations": True, "letalite": ":.1f",
                    "latitude": ":.2f", "longitude": ":.2f"},
    )
