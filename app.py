import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Compound Returns Calculator",
    page_icon="chart_with_upwards_trend",
    layout="centered")

# CSS = """
# iframe {
#     width: 50%
# }
# img {
#     display: block;
#     margin-left: center;
#     margin-right: center;
#     width: 50%;
# }

# """

# st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

st.write("# Compound Return Calculator")

# user input
initial = st.number_input(
    label='Initial Amount',
    value=0.0,
    step=1000.0
    )

monthly_savings = st.number_input(
    label='Monthly Savings',
    value=0.0,
    step=100.0
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
    value=0,
    step=1
    )

# calculation and display
if st.button('Calculate'):

    ## method 1
    # I = initial
    # S = savings * 12
    # RS = 1 + savings_growth / 100
    # net_returns = returns * (1 - tax_rate / 100)
    # RI = 1 + net_returns / 100
    # N = years - 1

    # try:
    #     result = I * RI**N \
    #             + S * RI**N * ((RS/RI)**(N+1)-1) / ((RS/RI)-1)
    #     st.metric('Result', f'{round(result,2):,}')
    # except ZeroDivisionError:
    #     st.write("""Zero Division Error: Choose different values
    #              for net return and savings increase.""")

    ## method 2
    net_returns = returns * (1 - tax_rate / 100)

    # dataframe initialize
    df = pd.DataFrame(
        {
            "Year": list(range(1, years + 1)),
            "Previous": [initial] + [np.nan]*(years-1),
            "Returns": [np.nan]*years,
            "Invested": [np.nan]*years,
            "End": [np.nan]*years
        }
    )

    df = df.set_index("Year")

    # iterate
    for i in range(1, years + 1):
        if i > 1:
            df.loc[i, "Previous"] = end
        df.loc[i, "Returns"] = df.loc[i, "Previous"] * net_returns / 100
        df.loc[i, "Invested"] = (monthly_savings * 12) * (1 + savings_growth / 100)**i
        end = df.loc[i].sum()
        df.loc[i, "End"] = end

    st.metric('Final amount', f'{round(df.iloc[-1,-1],2):,}')

    # plot
    width = 0.35
    fig, ax = plt.subplots()

    ax.bar(df.index, df.Previous, width, label='Previous')
    ax.bar(df.index, df.Invested, width, bottom=df.Previous, label='Invested')
    ax.bar(df.index, df.Returns, width, bottom=df.Previous + df.Invested, label='Gains')

    ax.set_ylabel('$')
    ax.set_xlabel('Year')
    ax.set_title('Portfolio Development by Year')
    ax.legend()
    ax.set_xticks(df.index)
    st.pyplot(fig)

# Made by Ruben Rossbach, GH LI
