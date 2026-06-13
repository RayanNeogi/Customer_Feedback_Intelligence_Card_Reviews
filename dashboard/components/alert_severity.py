import streamlit as st


def alert_severity(df):

    st.header(
        "🚨 Executive Alert Center"
    )

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    total = len(df)

    negative_pct = (
        len(
            df[
                df["sentiment"]
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
                .str.lower()
                == "high"
            ]
        )
        / total
    ) * 100

    if negative_pct > 40:

        st.error(
            f"🔴 CRITICAL: Negative feedback is {negative_pct:.1f}%"
        )

    elif negative_pct > 25:

        st.warning(
            f"🟡 WARNING: Negative feedback is {negative_pct:.1f}%"
        )

    else:

        st.info(
            f"🔵 INFO: Negative feedback is {negative_pct:.1f}%"
        )

    if high_priority_pct > 30:

        st.error(
            f"🔴 CRITICAL: High priority feedback is {high_priority_pct:.1f}%"
        )

    elif high_priority_pct > 15:

        st.warning(
            f"🟡 WARNING: High priority feedback is {high_priority_pct:.1f}%"
        )

    else:

        st.info(
            f"🔵 INFO: High priority feedback is {high_priority_pct:.1f}%"
        )