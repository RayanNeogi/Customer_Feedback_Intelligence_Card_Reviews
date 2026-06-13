import streamlit as st
import pandas as pd

from database.repository import (
    insert_feedback
)

from src.pipeline1.nlp_pipeline import (
   process_feedback
)



def upload_csv():

    st.header(
        "📤 Upload Raw Feedback CSV"
    )

    uploaded_file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        raw_df = pd.read_csv(
            uploaded_file
        )

        # Ensure feedback_text exists

        if "feedback_text" not in raw_df.columns:

            if "text" in raw_df.columns:

                raw_df = raw_df.rename(
                    columns={
                        "text": "feedback_text"
                    }
                )

            else:

                st.error(
                    "CSV must contain a feedback_text column."
                )

                return

        st.success(
            f"{len(raw_df)} rows loaded."
        )

        st.subheader(
            "Raw Data Preview"
        )

        st.dataframe(
            raw_df.head()
        )

        if st.button(
            "🚀 Run NLP Pipeline & Store"
        ):

            with st.spinner(
                "Running AI pipeline..."
            ):

                processed_df = process_feedback(
                    raw_df
                )
              
                st.write("Processed Columns:")
                st.write(processed_df.columns.tolist())

                st.write(processed_df.head())
                st.write("Rows about to insert:", len(processed_df))
                st.write(processed_df.head())
                insert_feedback(
                    processed_df
                )
                insert_feedback(processed_df)

                st.success("INSERT FUNCTION FINISHED")

            st.success(
                "Pipeline completed successfully."
            )

            st.subheader(
                "Processed Data Preview"
            )

            st.dataframe(
                processed_df.head()
            )