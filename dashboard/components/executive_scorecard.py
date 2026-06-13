import streamlit as st


def executive_scorecard(df):

    st.header(
        "🏆 Executive Scorecard"
    )

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    total = len(df)

    negative = len(
        df[
            df["sentiment"]
            .str.lower()
            == "negative"
        ]
    )

    high_priority = len(
        df[
            df["priority"]
            .str.lower()
            == "high"
        ]
    )

    sentiment_score = max(
        0,
        100 - (
            negative / total * 100
        )
    )

    risk_score = max(
        0,
        100 - (
            high_priority / total * 100
        )
    )

    health_score = round(
        (
            sentiment_score +
            risk_score
        ) / 2,
        1
    )

    if health_score >= 80:

        status = "🟢 Healthy"

    elif health_score >= 60:

        status = "🟡 Moderate"

    else:

        status = "🔴 Critical"

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Health Score",
            f"{health_score}"
        )

    with col2:

        st.metric(
            "Sentiment Score",
            f"{sentiment_score:.1f}"
        )

    with col3:

        st.metric(
            "Risk Score",
            f"{risk_score:.1f}"
        )

    st.success(
        f"Overall Status: {status}"
    )