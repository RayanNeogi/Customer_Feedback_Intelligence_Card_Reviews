import pandas as pd

from src.sentiment.sentiment_analyzer import (
    SentimentAnalyzer
)


def calculate_accuracy(expected, predicted):

    correct = 0

    for e, p in zip(expected, predicted):

        if e == p:
            correct += 1

    return correct / len(expected)


analyzer = SentimentAnalyzer()

df = pd.read_csv(
    "data/Evaluation/sentiment_dataset.csv"
)

expected_labels = []
predicted_labels = []

for _, row in df.iterrows():

    text = row["text"]

    expected = (
        row["expected_sentiment"]
        .strip()
        .lower()
    )

    result = analyzer.analyze(text)

    predicted = (
        result["sentiment"]
        .strip()
        .lower()
    )

    expected_labels.append(expected)
    predicted_labels.append(predicted)

    print("\n" + "=" * 50)

    print(f"Text: {text}")

    print(f"Expected: {expected}")

    print(f"Predicted: {predicted}")

accuracy = calculate_accuracy(
    expected_labels,
    predicted_labels
)

print("\n" + "=" * 60)

print("SENTIMENT ANALYSIS RESULTS")

print("=" * 60)

print(
    f"Accuracy: {accuracy:.3f}"
)