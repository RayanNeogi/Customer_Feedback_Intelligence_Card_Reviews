import pandas as pd

from src.keyword_extraction.tfidf_extractor import TFIDFExtractor


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


# Load TF-IDF extractor
extractor = TFIDFExtractor()

# Load evaluation dataset
df = pd.read_csv(
    "src/evaluation/evaluation_dataset.csv"
)

all_precisions = []
all_recalls = []
all_f1s = []

for _, row in df.iterrows():

    text = row["text"]

    expected = [
        keyword.strip()
        for keyword in row["expected_keywords"].split(",")
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

    print("-" * 60)
    print(f"Text: {text}")
    print(f"Expected: {expected}")
    print(f"Predicted: {predicted}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1: {f1:.3f}")

print("\n" + "=" * 60)
print("TF-IDF BASELINE RESULTS")
print("=" * 60)

avg_precision = sum(all_precisions) / len(all_precisions)
avg_recall = sum(all_recalls) / len(all_recalls)
avg_f1 = sum(all_f1s) / len(all_f1s)

print(f"Average Precision: {avg_precision:.3f}")
print(f"Average Recall:    {avg_recall:.3f}")
print(f"Average F1 Score:  {avg_f1:.3f}")