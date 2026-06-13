from src.keyword_extraction.yake_extractor import YAKEExtractor
from src.sentiment.sentiment_analyzer import SentimentAnalyzer
from src.categorization.feedback_categorizer import FeedbackCategorizer
from src.categorization.priority_scorer import PriorityScorer


class FeedbackAnalyzer:

    def __init__(self):

        self.keyword_extractor = YAKEExtractor()

        self.sentiment_analyzer = SentimentAnalyzer()

        self.categorizer = FeedbackCategorizer()

        self.priority_scorer = PriorityScorer()

    def analyze(self, text):

        keywords = (
            self.keyword_extractor
            .extract_keyword_names(text)
        )

        sentiment_result = (
            self.sentiment_analyzer
            .analyze(text)
        )

        category = (
            self.categorizer
            .categorize(text)
        )

        priority = (
            self.priority_scorer
            .score(
                sentiment_result["sentiment"],
                category
            )
        )

        return {

            "keywords": keywords,

            "sentiment":
                sentiment_result["sentiment"],

            "category":
                category,

            "priority":
                priority
        }

if __name__ == "__main__":

    analyzer = FeedbackAnalyzer()

    text = (
        "My card was charged twice "
        "during payment."
    )

    result = analyzer.analyze(text)

    print(result)
    