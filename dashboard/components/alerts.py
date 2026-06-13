import streamlit as st


def render_alerts(df):

    total_feedback = len(df)

    negative_count = len(
        df[df["sentiment"] == "negative"]
    )

    negative_pct = (
        negative_count / total_feedback * 100
        if total_feedback > 0
        else 0
    )

    high_priority = len(
        df[df["priority"] == "High"]
    )

    fraud_count = len(
        df[
            df["category"]
            .str.contains(
                "Fraud",
                case=False,
                na=False
            )
        ]
    )

    alerts = []

    if negative_pct > 40:
        alerts.append(
            "High negative sentiment detected."
        )

    if high_priority > 5:
        alerts.append(
            "Large number of high priority issues."
        )

    if fraud_count > 0:
        alerts.append(
            f"{fraud_count} fraud complaints detected."
        )

    if alerts:

        for alert in alerts:
            st.error(alert)

    else:
        st.success(
            "No critical alerts."
        )