import spacy
import pytextrank


class TextRankExtractor:

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

        self.nlp.add_pipe("textrank")

    def extract_keywords(self, text, top_n=10):

        doc = self.nlp(text)

        keywords = []

        for phrase in doc._.phrases[:top_n]:

            keywords.append(
                (phrase.text, phrase.rank)
            )

        return keywords

    def extract_keyword_names(self, text, top_n=10):

        keywords = self.extract_keywords(
            text,
            top_n
        )

        return [
            keyword
            for keyword, score in keywords
        ]


if __name__ == "__main__":

    extractor = TextRankExtractor()

    sample_text = (
        "My card payment failed during checkout "
        "even though I had sufficient balance."
    )

    print("TextRank Keywords:")
    print(
        extractor.extract_keywords(sample_text)
    )

    print("\nKeyword Names:")
    print(
        extractor.extract_keyword_names(sample_text)
    )
    