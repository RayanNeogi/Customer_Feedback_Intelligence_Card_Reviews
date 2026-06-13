import pandas as pd

from src.pipeline1.feedback_analyzer import (
    FeedbackAnalyzer
)


class BatchAnalyzer:

    def __init__(self):

        self.analyzer = FeedbackAnalyzer()

    def process_dataset(
        self,
        input_file,
        output_file=None
    ):

        df = pd.read_csv(input_file)

        results = []

        for _, row in df.iterrows():

            feedback = str(
                row["feedback_text"]
            )

            analysis = self.analyzer.analyze(
                feedback
            )

            results.append(
                {
                    "feedback_text": feedback,

                    "predicted_sentiment":
                        analysis["sentiment"],

                    "predicted_category":
                        analysis["category"],

                    "priority":
                        analysis["priority"],

                    "keywords":
                        ", ".join(
                            analysis["keywords"]
                        )
                }
            )

        output_df = pd.DataFrame(
            results
        )

        if output_file:

            output_df.to_csv(
                output_file,
                index=False
            )

        return output_df


if __name__ == "__main__":

    analyzer = BatchAnalyzer()

    output = analyzer.process_dataset(
        input_file="data/Raw/customer_feedback.csv",
        output_file="data/processed_feedback.csv"
    )

    print(
        "\nProcessed Feedback Dataset\n"
    )

    print(
        output.head()
    )