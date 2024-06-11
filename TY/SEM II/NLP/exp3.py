import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
text = nltk.word_tokenize("And now for Everything completely Same")
nltk.pos_tag(text)
