import streamlit as st
import pandas as pd


def ai_copilot(df):

    st.header(
        "🤖 AI Executive Copilot"
    )

    question = st.text_input(
        "Ask a question about customer feedback"
    )

    if not question:

        return

    question = question.lower()

    # ==================================================
    # Most Negative Category
    # ==================================================

    if (
        "negative" in question
        and "category" in question
    ):

        negative_df = df[
            df["sentiment"]
            .astype(str)
            .str.lower()
            == "negative"
        ]

        if len(negative_df) > 0:

            top_category = (
                negative_df["category"]
                .value_counts()
                .idxmax()
            )

            st.success(
                f"""
The category with the most
negative feedback is:

{top_category}
"""
            )

        return

    # ==================================================
    # Top Category
    # ==================================================

    if "top category" in question:

        top_category = (
            df["category"]
            .value_counts()
            .idxmax()
        )

        st.success(
            f"""
Top Feedback Category:

{top_category}
"""
        )

        return

    # ==================================================
    # High Priority
    # ==================================================

    if "high priority" in question:

        count = len(
            df[
                df["priority"]
                .astype(str)
                .str.lower()
                == "high"
            ]
        )

        st.success(
            f"""
There are

{count}

high-priority feedback records.
"""
        )

        return

    # ==================================================
    # Summary
    # ==================================================

    if "summary" in question:

        total = len(df)

        negative = len(
            df[
                df["sentiment"]
                .astype(str)
                .str.lower()
                == "negative"
            ]
        )

        top_category = (
            df["category"]
            .value_counts()
            .idxmax()
        )

        st.success(
            f"""
Executive Summary

Total Feedback:
{total}

Negative Feedback:
{negative}

Top Category:
{top_category}
"""
        )

        return

    # ==================================================
    # Root Cause Analysis
    # ==================================================

    if "root cause" in question:

        if "keywords" in df.columns:

            all_keywords = []

            for row in df[
                "keywords"
            ].dropna():

                words = [
                    word.strip()
                    for word in str(row).split(",")
                ]

                all_keywords.extend(
                    words
                )

            if len(all_keywords) > 0:

                top_keywords = (
                    pd.Series(
                        all_keywords
                    )
                    .value_counts()
                    .head(5)
                    .index
                    .tolist()
                )

                output = (
                    "Top Root Causes:\n\n"
                )

                for keyword in top_keywords:

                    output += (
                        f"• {keyword}\n"
                    )

                st.success(
                    output
                )

        return

    # ==================================================
    # Recommendations
    # ==================================================

    if (
        "recommend" in question
        or
        "recommendation" in question
    ):

        negative_df = df[
            df["sentiment"]
            .astype(str)
            .str.lower()
            == "negative"
        ]

        if len(negative_df) > 0:

            top_category = (
                negative_df["category"]
                .value_counts()
                .idxmax()
            )

            st.success(
                f"""
Recommended Action

Focus on improving:

{top_category}

This category generates
the highest volume of
negative customer feedback.
"""
            )

        return

    # ==================================================
    # Sentiment Breakdown
    # ==================================================

    if "sentiment" in question:

        sentiment_counts = (
            df["sentiment"]
            .value_counts()
        )

        st.success(
            sentiment_counts.to_string()
        )

        return

    # ==================================================
    # Default
    # ==================================================

    st.info(
        """
I don't know how to answer that yet.

Try:

• summary

• root cause

• recommendation

• top category

• high priority

• which category has the most negative feedback

• sentiment
"""
    )