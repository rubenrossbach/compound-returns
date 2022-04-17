import streamlit as st

st.set_page_config(
    page_title="Compound Returns Calculator",
    page_icon="chart_with_upwards_trend",
    layout="wide")

CSS = """
iframe {
    width: 100%
}
img {
    display: block;
    margin-left: center;
    margin-right: center;
    width: 50%;
    border-radius: 50%;
}

"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

st.write("# Compound Return Calculator")
