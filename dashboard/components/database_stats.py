import streamlit as st


def database_stats(df):

    st.subheader(
        "🗄️ Database Statistics"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Rows Stored",
            len(df)
        )

    with col2:

        st.metric(
            "Columns",
            len(df.columns)
        )

    with col3:

        st.metric(
            "Categories",
            df["category"].nunique()
        )