import streamlit as st
import plotly.express as px


def sentiment_chart(df):

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


def category_chart(df):

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
        title="Category Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def priority_chart(df):

    priority_counts = (
        df["priority"]
        .value_counts()
        .reset_index()
    )

    priority_counts.columns = [
        "Priority",
        "Count"
    ]

    fig = px.bar(
        priority_counts,
        x="Priority",
        y="Count",
        title="Priority Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )