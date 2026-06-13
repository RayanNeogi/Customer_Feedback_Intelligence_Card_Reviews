class PriorityScorer:

    def score(
        self,
        sentiment,
        category
    ):

        if category == "Payment Issue":
            return "High"

        if category == "Login Issue":
            return "High"

        if sentiment == "negative":
            return "Medium"

        if sentiment == "neutral":
            return "Low"

        return "Low"

if __name__ == "__main__":

    scorer = PriorityScorer()

    print(
        scorer.score(
            "negative",
            "Payment Issue"
        )
    )

    print(
        scorer.score(
            "negative",
            "Feature Request"
        )
    )

    print(
        scorer.score(
            "positive",
            "Feature Request"
        )
    )
    