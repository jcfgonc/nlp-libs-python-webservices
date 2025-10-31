import logging

from flask import Flask, request

import nlp_spacy_main

app = Flask(__name__)


# greet_lock = threading.Lock()


@app.route("/")
def index() -> str:
	return "<h1>Hello!</h1>"


@app.route("/api/pos", methods=["GET"])
def pos() -> str:
	concept: str = request.args.get("concept")
	getpos: str = nlp_spacy_main.get_part_of_speech(concept)
	return getpos


@app.route("/api/constituency", methods=["GET"])
def constituency() -> str:
	concept: str = request.args.get("concept")
	cons: str = nlp_spacy_main.get_constituency(concept)
	return cons


@app.route("/api/clean", methods=["GET"])
def clean() -> str:
	concept: str = request.args.get("concept")
	cons: str = nlp_spacy_main.strip_dets_and_singularize(concept)
	return cons


if __name__ == "__main__":
	#	print(nlp_spacy_main.get_constituency("This text is used to warm-up the spacy library."))
	app.logger.disabled = True
	logging.getLogger('werkzeug').disabled = True
	app.run(host="0.0.0.0", port=80, threaded=True)
