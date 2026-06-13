import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import pandas as pd

from database.repository import (
    insert_feedback
)

df = pd.read_csv(
    "data/processed_feedback.csv"
)

insert_feedback(df)

print(
    f"{len(df)} records loaded successfully."
)