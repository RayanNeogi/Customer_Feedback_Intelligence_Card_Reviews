import streamlit as st


def generate_recommendations(df):

    st.subheader(
        "AI Recommendations"
    )

    top_category = (
        df["category"]
        .mode()[0]
        if not df.empty
        else None
    )

    recommendations = {

        "Payment Issue":
        "Review payment gateway failures and transaction retry logic.",

        "Fraud Concern":
        "Strengthen fraud detection workflows and customer notification systems.",

        "Customer Service":
        "Improve agent response time and support quality.",

        "Mobile App":
        "Investigate crash logs and mobile performance bottlenecks.",

        "Rewards Issue":
        "Audit reward point calculation and redemption flows."
    }

    if top_category in recommendations:

        st.info(
            recommendations[top_category]
        )

    else:

        st.info(
            "No recommendations available."
        )