import streamlit as st
import pandas as pd
import plotly.express as px


def sentiment_heatmap(df):

    st.header(
        "🔥 Sentiment vs Category Heatmap"
    )

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    heatmap_df = pd.crosstab(
        df["category"],
        df["sentiment"]
    )

    st.subheader(
        "Sentiment Distribution by Category"
    )

    st.dataframe(
        heatmap_df,
        use_container_width=True
    )

    fig = px.imshow(
        heatmap_df,
        text_auto=True,
        aspect="auto",
        title="Category vs Sentiment"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Executive Insight

    st.subheader(
        "📌 Key Observations"
    )

    try:

        negative_col = None

        for col in heatmap_df.columns:

            if str(col).lower() == "negative":

                negative_col = col
                break

        if negative_col:

            highest_negative = (
                heatmap_df[negative_col]
                .idxmax()
            )

            highest_negative_count = (
                heatmap_df[negative_col]
                .max()
            )

            st.info(
                f"""
Most negative feedback comes from
'{highest_negative}'
with {highest_negative_count}
negative responses.
"""
            )

    except Exception:

        pass