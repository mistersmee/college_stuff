import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from langid.langid import LanguageIdentifier, model

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "KIT’S COLLEGE OF ENGINEERING IS THE BEST ENGINEERING COLLEGE IN MAHARASHTRA. "

# Tokenization
tokens = word_tokenize(text)

# Language detection
identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
lang, confidence = identifier.classify(text)
print(f"Detected Language: {lang}, Confidence: {confidence}")

# Stop word removal
filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]

# Stemming
porter_stemmer = PorterStemmer()
stemmed_tokens = [porter_stemmer.stem(word) for word in filtered_tokens]

# Display the results
print("\nOriginal Tokens:")
print(tokens)
print("\nFiltered Tokens (After Stop Word Removal):")
print(filtered_tokens)
print("\nStemmed Tokens:")
print(stemmed_tokens)
