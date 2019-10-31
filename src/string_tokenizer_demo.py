from nltk.tokenize import sent_tokenize, word_tokenize


def tokenizer_demo():
	EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? "\
					"The weather is great, and Python is awesome. "\
					"The sky is pinkish-blue. You shouldn't eat cardboard."
	print(EXAMPLE_TEXT)
	print("sentence tokenize")
	print(sent_tokenize(EXAMPLE_TEXT))
	print("word tokenize")
	print(word_tokenize(EXAMPLE_TEXT))

if __name__ == "__main__":
	tokenizer_demo()
