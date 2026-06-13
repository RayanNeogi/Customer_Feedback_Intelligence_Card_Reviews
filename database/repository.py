from database.db import get_connection
import pandas as pd


def insert_feedback(df):

    print("\n========== DATAFRAME COLUMNS ==========")
    print(df.columns.tolist())
    print("=======================================\n")

    required_columns = [
        "feedback_text",
        "sentiment",
        "category",
        "priority",
        "keywords"
    ]

    df = df[required_columns]

    conn = get_connection()

    df.to_sql(
        "feedback",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()

    print(f"{len(df)} rows inserted successfully")


def get_feedback():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM feedback",
        conn
    )

    conn.close()

    return df