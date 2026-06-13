import pandas as pd
import time

from src.keyword_extraction.yake_extractor import YAKEExtractor


def calculate_precision(expected, predicted):
    expected = set(expected)
    predicted = set(predicted)

    if len(predicted) == 0:
        return 0

    return len(expected.intersection(predicted)) / len(predicted)


def calculate_recall(expected, predicted):
    expected = set(expected)
    predicted = set(predicted)

    if len(expected) == 0:
        return 0

    return len(expected.intersection(predicted)) / len(expected)


def calculate_f1(precision, recall):

    if precision + recall == 0:
        return 0

    return 2 * precision * recall / (precision + recall)


extractor = YAKEExtractor()

df = pd.read_csv(
    "src/evaluation/evaluation_dataset.csv"
)

all_precisions = []
all_recalls = []
all_f1s = []

start_time = time.time()

for _, row in df.iterrows():

    text = row["text"]

    expected = [
        x.strip()
        for x in row["expected_keywords"].split(",")
    ]

    predicted = extractor.extract_keyword_names(text)

    precision = calculate_precision(
        expected,
        predicted
    )

    recall = calculate_recall(
        expected,
        predicted
    )

    f1 = calculate_f1(
        precision,
        recall
    )

    all_precisions.append(precision)
    all_recalls.append(recall)
    all_f1s.append(f1)

runtime = time.time() - start_time

print("\nYAKE RESULTS\n")

print(
    f"Average Precision: "
    f"{sum(all_precisions)/len(all_precisions):.3f}"
)

print(
    f"Average Recall: "
    f"{sum(all_recalls)/len(all_recalls):.3f}"
)

print(
    f"Average F1 Score: "
    f"{sum(all_f1s)/len(all_f1s):.3f}"
)

print(
    f"Runtime: {runtime:.3f} sec"
)