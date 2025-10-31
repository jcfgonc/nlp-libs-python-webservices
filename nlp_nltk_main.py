from typing import TextIO
import nltk, time
from nltk.tokenize import word_tokenize

def get_part_of_speech(concept: str) -> str:
	text: list[str] = word_tokenize(f'{concept}.')
	tagged_tokens = nltk.pos_tag(text)
	retval: str = ""
	for tt in tagged_tokens:
		retval += tt[1] + ' '
	return retval


# Defining main function
def main():

	file: TextIO = open("D:/My Source Code/Java - PhD/MapperMO/newconcepts.txt", "r", encoding="utf8")
	lines: list[str] = file.read().splitlines()
	file.close()

	for concept in lines:
		print(f'{concept}\t{get_part_of_speech(concept)}')


if __name__ == "__main__":
	main()
