import streamlit as st
from torch import initial_seed

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

# user input
initial = st.number_input(
    label='Inital Amount',
    value=0.0,
    step=1.0
    )

savings = st.number_input(
    label='Monthly Savings',
    value=0.0,
    step=1.0
    )

savings_growth = st.number_input(
    label='Annual Savings Increase (%)',
    value=0.0,
    step=1.0
    )

returns = st.number_input(
    label='Expected Return (%)',
    value=8.0,
    step=1.0
    )

tax_rate = st.number_input(
    label='Tax Rate (%)',
    value=0.0,
    step=1.0
    )

years = st.number_input(
    label='Number of Years',
    value=0.0,
    step=1.0
    )

# calculation
if st.button('Calculate'):
    I = initial
    S = savings * 12
    RS = 1 + savings_growth / 100
    net_returns = returns * (1 - tax_rate / 100)
    RI = 1 + net_returns / 100
    N = years - 1

    try:
        result = I * RI**N \
                + S * RI**N * ((RS/RI)**(N+1)-1) / ((RS/RI)-1)
        st.metric('Result', f'{round(result,2):,}')
    except ZeroDivisionError:
        st.write("""Zero Division Error: Choose different values
                 for net return and savings increase.""")

# display: create bar chart
