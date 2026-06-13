import streamlit as st


def show_trends(df):

    st.subheader("Category Trends")

    category_counts = (
        df["category"]
        .value_counts()
        .reset_index()
    )

    category_counts.columns = [
        "Category",
        "Count"
    ]

    st.bar_chart(
        category_counts.set_index(
            "Category"
        )
    )