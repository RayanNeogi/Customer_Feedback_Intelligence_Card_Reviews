import pickle


class TFIDFExtractor:

    def __init__(self):

        self.cv = pickle.load(
            open(
                "models/keywords-count-vectorizer.pkl",
                "rb"
            )
        )

        self.tfidf = pickle.load(
            open(
                "models/keywords-tfidf-model.pkl",
                "rb"
            )
        )

        self.feature_names = pickle.load(
            open(
                "models/keywords-feature-names.pkl",
                "rb"
            )
        )

    def extract_keywords(self, text):
        """
        Returns top keywords along with their TF-IDF scores.
        Example:
        [
            ('card', 0.88),
            ('payment', 0.74),
            ('checkout', 0.61)
        ]
        """

        vector = self.tfidf.transform(
            self.cv.transform([text])
        )

        scores = vector.toarray()[0]

        pairs = list(
            zip(self.feature_names, scores)
        )

        pairs = sorted(
            pairs,
            key=lambda x: x[1],
            reverse=True
        )

        return [
            (word, score)
            for word, score in pairs[:10]
            if score > 0
        ]

    def extract_keyword_names(self, text):
        """
        Returns only the keyword names.
        Example:
        ['card', 'payment', 'checkout']
        """

        keywords = self.extract_keywords(text)

        return [
            word
            for word, score in keywords
        ]


if __name__ == "__main__":

    extractor = TFIDFExtractor()

    sample_text = (
        "My card payment failed during checkout "
        "even though I had sufficient balance."
    )

    print("Keywords with scores:")
    print(extractor.extract_keywords(sample_text))

    print("\nKeyword names only:")
    print(extractor.extract_keyword_names(sample_text))