import streamlit as st


def customer_voice(df):

    st.header(
        "🗣 Customer Voice"
    )

    if df.empty:

        st.warning(
            "No feedback available."
        )

        return

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "😊 Top Positive Feedback"
        )

        positive_df = df[
            df["sentiment"]
            .astype(str)
            .str.lower() == "positive"
        ]

        if len(positive_df) > 0:

            for text in (
                positive_df["feedback_text"]
                .head(5)
            ):

                st.success(text)

        else:

            st.info(
                "No positive feedback."
            )

    with col2:

        st.subheader(
            "😡 Top Negative Feedback"
        )

        negative_df = df[
            df["sentiment"]
            .astype(str)
            .str.lower() == "negative"
        ]

        if len(negative_df) > 0:

            for text in (
                negative_df["feedback_text"]
                .head(5)
            ):

                st.error(text)

        else:

            st.info(
                "No negative feedback."
            )