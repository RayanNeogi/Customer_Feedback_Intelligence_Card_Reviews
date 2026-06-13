import streamlit as st
import pandas as pd
from collections import Counter
import plotly.express as px


def root_cause_analysis(df):

    st.header(
        "🧠 Root Cause Analysis"
    )

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    if "keywords" not in df.columns:

        st.warning(
            "Keywords column missing."
        )

        return

    category_keywords = {}

    for _, row in df.iterrows():

        category = str(
            row["category"]
        )

        keywords = str(
            row["keywords"]
        ).split(",")

        keywords = [
            keyword.strip()
            for keyword in keywords
            if keyword.strip()
        ]

        if category not in category_keywords:

            category_keywords[
                category
            ] = []

        category_keywords[
            category
        ].extend(
            keywords
        )

    results = []

    st.subheader(
        "Top Causes By Category"
    )

    for category, words in category_keywords.items():

        top_words = Counter(
            words
        ).most_common(5)

        st.markdown(
            f"### {category}"
        )

        for word, count in top_words:

            st.write(
                f"• {word} ({count})"
            )

            results.append(
                {
                    "Category": category,
                    "Keyword": word,
                    "Frequency": count
                }
            )

    if len(results) > 0:

        chart_df = pd.DataFrame(
            results
        )

        fig = px.treemap(
            chart_df,
            path=[
                "Category",
                "Keyword"
            ],
            values="Frequency",
            title="Root Cause Treemap"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )