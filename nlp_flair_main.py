from flair.nn import Classifier
from flair.data import Sentence
from typing import TextIO

pos_tagger = Classifier.load('pos')
chunk_tagger = Classifier.load('chunk')

def get_part_of_speech(concept: str) -> str:
	sentence: Sentence = Sentence(f'{concept}.')
	pos_tagger.predict(sentence)
	retval: str = ""
	for token in sentence:
		retval += token.tag + ' '	
	return retval

def get_constituency(concept: str) -> str:
	sentence: Sentence = Sentence(f'{concept}.')
	chunk_tagger.predict(sentence)
	retval: str = ""
	for label in sentence.labels:
		retval += label.value + ' '
	return retval

# Defining main function
def main():

	file: TextIO = open("D:/My Source Code/Java - PhD/MapperMO/newconcepts.txt", "r", encoding="utf8")
	lines: list[str] = file.read().splitlines()
	file.close()

	for concept in lines:
		print(f'{concept}\t{get_constituency(concept)}')


if __name__ == "__main__":
	main()
