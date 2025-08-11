import streamlit as st
st.set_page_config(page_title="AI Real Estate Analyzer", layout="wide")

st.title("AI-Powered Real Estate Investment Analyzer")
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Go to", ["Overview","ROI & Cash-Flow","Rent Forecasts","Market Sentiment","Recommendations"])

if page == "Overview":
    st.write("Welcome! Use the sidebar to navigate modules.")
elif page == "ROI & Cash-Flow":
    st.subheader("Quick ROI / Gross Yield")
    price = st.number_input("Purchase price", min_value=0, step=1000)
    rent = st.number_input("Monthly rent", min_value=0, step=50)
    expenses = st.number_input("Monthly expenses (tax, insurance, HOA, etc.)", min_value=0, step=50)

    if price > 0:
        gross_yield = (rent * 12) / price
        annual_cash_flow = (rent - expenses) * 12
        st.metric("Gross yield", f"{gross_yield:.2%}")
        st.metric("Est. annual cash flow", f"{annual_cash_flow:,.0f} €")
    else:
        st.info("Enter a price to see yield.")

elif page == "Rent Forecasts":
    st.info("Prophet/ARIMA forecasts will appear here.")
elif page == "Market Sentiment":
    st.info("News ingestion + sentiment charts coming soon.")
else:
    st.info("Rule-based/ML ensemble recommender coming soon.")