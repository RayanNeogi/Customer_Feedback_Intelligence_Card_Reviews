import streamlit as st
import pandas as pd

from src.llm.gemini_service import ask_ai

def ai_copilot(df):

    st.header("AI Executive Copilot")

    st.write(
        "Ask questions about customer feedback, risks, trends, recommendations or customer sentiment."
    )

    question = st.text_area(
        "Executive Question",
        height=120,
        placeholder="Example: Why are payment complaints increasing?"
    )

    if st.button("Ask AI"):

        if question.strip() == "":

            st.warning(
                "Please enter a question."
            )

            return

        with st.spinner(
            "Generating executive insights..."
        ):

            total_feedback = len(df)

            negative_feedback = len(
                df[
                    df["sentiment"]
                    .astype(str)
                    .str.lower()
                    == "negative"
                ]
            )

            positive_feedback = len(
                df[
                    df["sentiment"]
                    .astype(str)
                    .str.lower()
                    == "positive"
                ]
            )

            high_priority = len(
                df[
                    df["priority"]
                    .astype(str)
                    .str.lower()
                    == "high"
                ]
            )

            top_category = (
                df["category"]
                .mode()[0]
                if not df.empty
                else "N/A"
            )

            sentiment_distribution = (
                df["sentiment"]
                .value_counts()
                .to_dict()
            )

            category_distribution = (
                df["category"]
                .value_counts()
                .to_dict()
            )

            keyword_text = ""

            if "keywords" in df.columns:

                keywords = []

                for row in df["keywords"].dropna():

                    keywords.extend(
                        [
                            word.strip()
                            for word in str(row).split(",")
                        ]
                    )

                top_keywords = (
                    pd.Series(keywords)
                    .value_counts()
                    .head(15)
                    .to_dict()
                )

                keyword_text = str(
                    top_keywords
                )

            context = f"""
Total Feedback: {total_feedback}

Negative Feedback: {negative_feedback}

Positive Feedback: {positive_feedback}

High Priority Feedback: {high_priority}

Top Category: {top_category}

Sentiment Distribution:
{sentiment_distribution}

Category Distribution:
{category_distribution}

Top Keywords:
{keyword_text}
"""

            answer = ask_ai(
                question,
                context
            )

        st.markdown("---")

        st.subheader(
            "Executive Insight"
        )

        st.write(answer)