from typing import TextIO
import stanza, time, torch

nlp_stanza = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,constituency', download_method=None, use_gpu=True, pos_batch_size=3000)


def get_part_of_speech(concept: str) -> str:
#	start = time.time()
	doc = nlp_stanza(f'{concept}.')
	retval: str = ""
	for sent in doc.sentences:
		for word in sent.words:
			retval += str(word.xpos) + ' '
	#			print(f'{word.xpos}:{word.lemma}', end='\t')
#	end = time.time()
#	print(f'get_part_of_speech\t{end - start}')
	return retval


# for concept in lines:
# 	text = word_tokenize(concept)
# 	tagged_tokens = nltk.pos_tag(text)
# 	print(tagged_tokens)

def get_constituency(concept: str) -> str:
#	start = time.time()
	retval: str = ""
	doc = nlp_stanza(f'{concept}.')
	for sentence in doc.sentences:
		retval += str(sentence.constituency)
#	end = time.time()
#	print(f'get_constituency\t{end - start}')
	return retval


#	tree = doc.sentences[0].constituency
#	print(tree.children[0])

# Defining main function
def main():
	print(torch.__path__)

	print(f'TORCH:{torch.__version__} CUDA:{torch.cuda.is_available()}')

	file: TextIO = open("D:/My Source Code/Java - PhD/MapperMO/newconcepts.txt", "r", encoding="utf8")
	lines: list[str] = file.read().splitlines()
	file.close()

	for concept in lines:
		print(f'{concept}\t{get_constituency(concept)}')


if __name__ == "__main__":
	main()
