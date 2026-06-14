import streamlit as st

from components.executive_scorecard import (
    executive_scorecard
)

from components.alert_severity import (
    alert_severity
)

from components.customer_voice import (
    customer_voice
)

from components.recommendation_engine import (
    generate_recommendations
)


def overview(df):

    st.title(
        "📋 Executive Overview"
    )

    executive_scorecard(df)

    st.markdown("---")

    alert_severity(df)

    st.markdown("---")

    customer_voice(df)

    st.markdown("---")

    generate_recommendations(df)