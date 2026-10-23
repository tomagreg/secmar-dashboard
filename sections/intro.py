"""Section 1: hook, context, audience and data caveats."""

import streamlit as st

from utils.i18n import t


def render() -> None:
    """Render the hook, context and limits."""
    st.header(t("intro_header"))
    st.markdown(t("intro_hook"))
    st.markdown(t("intro_context"))
    st.info(t("intro_limits"))
