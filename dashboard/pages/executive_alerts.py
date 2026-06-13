import streamlit as st
from utils.data_loader import load_data

st.title("🚨 Executive Alert Center")

df = load_data()

critical = df[
    df["priority"].str.lower() == "high"
]

st.metric(
    "Critical Cases",
    len(critical)
)

st.dataframe(
    critical,
    use_container_width=True
)