import streamlit as st


def calculate_risk(df):

    st.header("⚠️ Business Risk Score")

    if len(df) == 0:

        st.warning(
            "No data available."
        )

        return

    total = len(df)

    negative_pct = (
        len(
            df[
                df["sentiment"]
                .astype(str)
                .str.lower()
                == "negative"
            ]
        )
        / total
    ) * 100

    high_priority_pct = (
        len(
            df[
                df["priority"]
                .astype(str)
                .str.lower()
                == "high"
            ]
        )
        / total
    ) * 100

    fraud_pct = (
        len(
            df[
                df["category"]
                .astype(str)
                .str.lower()
                .str.contains(
                    "fraud",
                    na=False
                )
            ]
        )
        / total
    ) * 100

    risk_score = (
        negative_pct * 0.4
        + high_priority_pct * 0.4
        + fraud_pct * 0.2
    )

    risk_score = min(
        round(risk_score),
        100
    )

    if risk_score >= 75:

        level = "HIGH"

    elif risk_score >= 50:

        level = "MEDIUM"

    else:

        level = "LOW"

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )

    with col2:

        st.metric(
            "Risk Level",
            level
        )

    st.progress(
        risk_score / 100
    )