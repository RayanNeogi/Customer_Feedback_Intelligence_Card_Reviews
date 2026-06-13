import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def show_wordcloud(df):

    st.header("☁️ NLP Word Cloud")

    if "keywords" not in df.columns:

        st.warning(
            "Keywords column not found."
        )

        return

    text = ""

    for row in df["keywords"].dropna():

        text += " " + str(row)

    if len(text.strip()) == 0:

        st.warning(
            "No keywords available."
        )

        return

    wordcloud = WordCloud(
        width=1200,
        height=500,
        background_color="white"
    ).generate(text)

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    ax.imshow(
        wordcloud,
        interpolation="bilinear"
    )

    ax.axis("off")

    st.pyplot(fig)