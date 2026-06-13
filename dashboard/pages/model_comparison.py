import streamlit as st
import pandas as pd

st.title(
    "🏆 Model Benchmark"
)

benchmark = pd.DataFrame({

    "Model": [
        "TF-IDF",
        "YAKE",
        "TextRank"
    ],

    "Precision": [
        0.275,
        0.283,
        0.100
    ],

    "Recall": [
        0.133,
        0.758,
        0.092
    ],

    "F1": [
        0.173,
        0.395,
        0.095
    ]
})

st.dataframe(
    benchmark,
    use_container_width=True
)

st.success(
    "YAKE selected as production model."
)