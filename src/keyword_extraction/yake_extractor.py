import yake


class YAKEExtractor:

    def __init__(
        self,
        language="en",
        max_ngram_size=3,
        deduplication_threshold=0.9,
        num_keywords=10
    ):

        self.extractor = yake.KeywordExtractor(
            lan=language,
            n=max_ngram_size,
            dedupLim=deduplication_threshold,
            top=num_keywords
        )

    def extract_keywords(self, text):

        keywords = self.extractor.extract_keywords(text)

        return keywords

    def extract_keyword_names(self, text):

        keywords = self.extract_keywords(text)

        return [
            keyword
            for keyword, score in keywords
        ]


if __name__ == "__main__":

    extractor = YAKEExtractor()

    sample_text = (
        "My card payment failed during checkout "
        "even though I had sufficient balance."
    )

    print("YAKE Keywords:")
    print(extractor.extract_keywords(sample_text))

    print("\nKeyword Names:")
    print(extractor.extract_keyword_names(sample_text))
    