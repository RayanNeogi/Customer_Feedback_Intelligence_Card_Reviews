import streamlit as st
import plotly.express as px


def sentiment_analytics(df):

    st.title("😊 Sentiment Analytics")

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    # ==========================
    # Sentiment Distribution
    # ==========================

    sentiment_counts = (
        df["sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_counts.columns = [
        "Sentiment",
        "Count"
    ]

    fig = px.pie(
        sentiment_counts,
        names="Sentiment",
        values="Count",
        title="Sentiment Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================
    # Sentiment by Category
    # ==========================

    category_sentiment = (
        df.groupby(
            ["category", "sentiment"]
        )
        .size()
        .reset_index(
            name="Count"
        )
    )

    fig = px.bar(
        category_sentiment,
        x="category",
        y="Count",
        color="sentiment",
        barmode="group",
        title="Sentiment by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )