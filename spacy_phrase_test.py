from typing import TextIO

import spacy

from nlp_spacy_main import get_constituency

# Load the English model
nlp = spacy.load("en_core_web_lg")


def classify_phrase(text):
    doc = nlp(text)
    # Remove leading/trailing whitespace and punctuation
    text = text.strip().strip('.,!?')
    # Check if the text matches any noun chunk in the doc
    for np in doc.noun_chunks:
        if np.text.lower() == text.lower():
            return "Noun Phrase"
    # Heuristic: If the first token is a verb, and the phrase is not a noun phrase
    first_token = doc[0]
    if first_token.pos_ in ("VERB", "AUX"):
        return "Verb Phrase "
    return "Unknown"


file: TextIO = open("D:\\Desktop\\Untitled-5.txt", "r", encoding="utf8")
lines: list[str] = file.read().splitlines()
file.close()

for phrase in lines:
#    print(f"'{phrase}': {get_constituency(phrase)}")
    print(f"{phrase}\t{classify_phrase(phrase)}\t{get_constituency(phrase)}")
