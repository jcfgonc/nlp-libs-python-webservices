import benepar
import spacy

benepar.download('benepar_en3')
# nlp = spacy.load("en_core_web_sm") #  12 MB
# nlp = spacy.load("en_core_web_md") #  31 MB
# nlp = spacy.load("en_core_web_lg") # 382 MB
nlp = spacy.load("en_core_web_trf")  # 436 MB

nlp.add_pipe("benepar", config={"model": "benepar_en3"})


def get_part_of_speech(concept: str) -> str:
	doc = nlp(concept)
	retval: str = ""
	for token in doc:
		#	print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
		retval += token.tag_ + ' '
	return retval


def get_constituency(concept: str) -> str:
	retval: str = ""
	doc = nlp(f"{concept}.")
	sent = list(doc.sents)[0]
	retval += str(sent._.parse_string)
	#	print(sent._.parse_string)
	return retval


def strip_dets_and_singularize(text: str) -> str:
	"""
	Return a new string where
	  • all determiners (the, a, an, this, those, …) are removed, and
	  • all common nouns are converted to their singular form.

	Parameters
	----------
	text : str
		Source sentence or paragraph.

	Returns
	-------
	str
		Text with determiners removed and nouns singularised.
	"""
	doc = nlp(text)
	pieces = []

	for tok in doc:
		# 1) Skip determiners entirely
		if tok.pos_ == "DET":
			continue

		# 2) Singularise common nouns with the lemma
		if tok.pos_ == "NOUN":
			form = tok.lemma_
			# keep original capitalisation (e.g. "Cats" -> "Cat")
			if tok.text.istitle():
				form = form.capitalize()
		else:
			form = tok.text

		# 3) Add the token followed by its original white‑space
		pieces.append(form + tok.whitespace_)

	result = "".join(pieces).strip()
	#print(f"{text}\t->\t{result}")
	return result


# Defining main function
def main():
	print(f'spaCy version: {spacy.__version__}')

	print(get_constituency("sukhoi su-57 operational squadron"))


#	file: TextIO = open("C:\\MySourceCode\\Java - PhD\\MapperMO\\concept_classes.txt", "r", encoding="utf8")
#	lines: list[str] = file.read().splitlines()
#	file.close()

#	for concept in lines:
#		print(f'{concept}\t{get_constituency(concept)}')


if __name__ == "__main__":
	main()
