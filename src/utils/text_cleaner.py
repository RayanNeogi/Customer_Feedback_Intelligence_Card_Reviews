import re
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words("english"))

CUSTOM_WORDS = [
    "fig",
    "figure",
    "image",
    "sample",
    "using",
    "show",
    "result",
    "large",
    "also",
    "one",
    "two",
    "three",
    "four",
    "five",
    "seven",
    "eight",
    "nine"
]

STOP_WORDS.update(CUSTOM_WORDS)


def preprocess(text):

    text = str(text).lower()

    text = re.sub(r"\d+", " ", text)

    text = re.sub(r"\W+", " ", text)

    tokens = text.split()

    tokens = [word for word in tokens if word not in STOP_WORDS]

    return " ".join(tokens)