from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:

    def __init__(self):

        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):

        scores = self.analyzer.polarity_scores(text)

        compound = scores["compound"]

        if compound >= 0.05:
            sentiment = "positive"

        elif compound <= -0.05:
            sentiment = "negative"

        else:
            sentiment = "neutral"

        return {
            "sentiment": sentiment,
            "scores": scores
        }


if __name__ == "__main__":

    analyzer = SentimentAnalyzer()

    samples = [

        "I love this app. Everything works perfectly.",

        "My payment failed again. Terrible experience.",

        "The application was updated yesterday."

    ]

    for text in samples:

        result = analyzer.analyze(text)

        print("\nText:")
        print(text)

        print("\nResult:")
        print(result)

        print("-" * 50)