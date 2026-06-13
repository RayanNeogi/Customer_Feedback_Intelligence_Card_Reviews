import streamlit as st


def render_kpis(df):

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

    top_category = (
        df["category"].mode()[0]
        if not df.empty
        else "N/A"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Feedback",
            total_feedback
        )

    with col2:
        st.metric(
            "Negative %",
            f"{negative_pct:.1f}%"
        )

    with col3:
        st.metric(
            "High Priority",
            high_priority
        )

    with col4:
        st.metric(
            "Top Category",
            top_category
        )