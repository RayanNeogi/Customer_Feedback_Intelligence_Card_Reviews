import streamlit as st
import plotly.express as px


def category_analytics(df):

    st.title(
        "📂 Category Analytics"
    )

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    # ==========================
    # Category Distribution
    # ==========================

    category_counts = (
        df["category"]
        .value_counts()
        .reset_index()
    )

    category_counts.columns = [
        "Category",
        "Count"
    ]

    fig = px.bar(
        category_counts,
        x="Category",
        y="Count",
        title="Feedback by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================
    # Category vs Priority
    # ==========================

    priority_df = (
        df.groupby(
            ["category", "priority"]
        )
        .size()
        .reset_index(
            name="Count"
        )
    )

    fig = px.bar(
        priority_df,
        x="category",
        y="Count",
        color="priority",
        barmode="group",
        title="Category vs Priority"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )