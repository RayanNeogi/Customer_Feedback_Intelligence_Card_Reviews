import streamlit as st


def generate_insights(df):

    st.header("🧠 Executive Insights")

    if len(df) == 0:

        st.warning(
            "No data available."
        )

        return

    insights = []

    # Top category

    top_category = (
        df["category"]
        .value_counts()
        .idxmax()
    )

    top_category_pct = (
        df["category"]
        .value_counts(normalize=True)
        .max()
        * 100
    )

    insights.append(
        f"{top_category} accounts for "
        f"{top_category_pct:.1f}% of all feedback."
    )

    # Negative sentiment

    negative_pct = (
        len(
            df[
                df["sentiment"]
                .str.lower()
                == "negative"
            ]
        )
        / len(df)
        * 100
    )

    if negative_pct > 40:

        insights.append(
            f"Negative sentiment is elevated "
            f"at {negative_pct:.1f}%."
        )

    # High priority

    high_priority_pct = (
        len(
            df[
                df["priority"]
                .str.lower()
                == "high"
            ]
        )
        / len(df)
        * 100
    )

    if high_priority_pct > 20:

        insights.append(
            f"High-priority issues represent "
            f"{high_priority_pct:.1f}% of all feedback."
        )

    # Fraud monitoring

    fraud_count = len(
        df[
            df["category"]
            .str.lower()
            .str.contains(
                "fraud",
                na=False
            )
        ]
    )

    if fraud_count > 0:

        insights.append(
            f"{fraud_count} fraud-related "
            f"complaints require monitoring."
        )

    for insight in insights:

        st.info(insight)