import streamlit as st
import pandas as pd
import plotly.express as px

from components.wordcloud_view import (
    show_wordcloud
)


def keyword_intelligence(df):

    st.title(
        "🔑 Keyword Intelligence"
    )

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    if "keywords" not in df.columns:

        st.warning(
            "Keywords column not found."
        )

        return

    all_keywords = []

    for row in df["keywords"].dropna():

        words = [
            word.strip()
            for word in str(row).split(",")
        ]

        all_keywords.extend(
            words
        )

    if len(all_keywords) == 0:

        st.info(
            "No keywords available."
        )

        return

    keyword_df = (
        pd.Series(all_keywords)
        .value_counts()
        .head(20)
        .reset_index()
    )

    keyword_df.columns = [
        "Keyword",
        "Frequency"
    ]

    st.subheader(
        "Top 20 Keywords"
    )

    st.dataframe(
        keyword_df,
        use_container_width=True
    )

    fig = px.bar(
        keyword_df,
        x="Keyword",
        y="Frequency",
        title="Keyword Frequency"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    show_wordcloud(df)