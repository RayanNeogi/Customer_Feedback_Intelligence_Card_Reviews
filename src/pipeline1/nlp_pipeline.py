from src.sentiment.sentiment_analyzer import (
    SentimentAnalyzer
)

from src.categorization.feedback_categorizer import (
    FeedbackCategorizer
)

from src.categorization.priority_scorer import (
    PriorityScorer
)

from src.keyword_extraction.tfidf_extractor import (
    TFIDFExtractor
)

sentiment_model = SentimentAnalyzer()

category_model = FeedbackCategorizer()

priority_model = PriorityScorer()

keyword_model = TFIDFExtractor()


def process_feedback(df):

    sentiments = []

    categories = []

    priorities = []

    keywords_list = []

    for text in df["feedback_text"]:

        text = str(text)

        sentiment_result = (
            sentiment_model.analyze(text)
        )

        sentiment = (
            sentiment_result["sentiment"]
        )

        category = (
            category_model.categorize(text)
        )

        priority = (
            priority_model.score(
                sentiment,
                category
            )
        )

        keywords = (
            keyword_model
            .extract_keyword_names(text)
        )

        sentiments.append(
            sentiment
        )

        categories.append(
            category
        )

        priorities.append(
            priority
        )

        keywords_list.append(
            ", ".join(keywords)
        )

    df["sentiment"] = sentiments

    df["category"] = categories

    df["priority"] = priorities

    df["keywords"] = keywords_list

    return df