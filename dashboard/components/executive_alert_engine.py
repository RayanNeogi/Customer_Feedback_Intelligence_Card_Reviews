import streamlit as st


def run_alert_engine(df):

    alerts = []

    total = len(df)

    if total == 0:
        return

    negative_pct = (
        len(
            df[
                df["sentiment"]
                .str.lower() == "negative"
            ]
        ) / total
    ) * 100

    if negative_pct > 40:
        alerts.append(
            f"🚨 Negative sentiment is high ({negative_pct:.1f}%)"
        )

    high_priority_pct = (
        len(
            df[
                df["priority"]
                .str.lower() == "high"
            ]
        ) / total
    ) * 100

    if high_priority_pct > 20:
        alerts.append(
            f"🚨 High priority issues are elevated ({high_priority_pct:.1f}%)"
        )

    fraud_count = len(
        df[
            df["category"]
            .str.lower()
            .str.contains("fraud")
        ]
    )

    if fraud_count > 0:
        alerts.append(
            f"🚨 Fraud-related complaints detected ({fraud_count})"
        )

    st.subheader("Executive Alerts")

    if alerts:

        for alert in alerts:
            st.error(alert)

    else:

        st.success(
            "No critical business alerts."
        )