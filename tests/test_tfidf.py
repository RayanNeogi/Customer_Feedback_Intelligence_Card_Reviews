import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from src.keyword_extraction.tfidf_extractor import TFIDFExtractor

extractor = TFIDFExtractor()

text = """
The payment gateway failed
during checkout and users
could not complete transactions.
"""

print(extractor.extract_keywords(text))
