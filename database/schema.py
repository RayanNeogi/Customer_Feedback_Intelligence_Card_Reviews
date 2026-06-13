import sqlite3


def create_feedback_table():

    conn = sqlite3.connect(
        "database/feedback.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (

            feedback_id INTEGER PRIMARY KEY,

            feedback_text TEXT,

            sentiment TEXT,

            category TEXT,

            priority TEXT,

            keywords TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()

    conn.close()