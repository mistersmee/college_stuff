import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Tokenize the text
    words = word_tokenize(text)
    # Lowercasing
    words = [word.lower() for word in words]
     # Remove punctuation
    words = [word for word in words if word.isalnum()]
    return words


def perform_morphological_analysis(words):
    # Stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]
    return lemmatized_words

def remove_stop_words(words):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def main():
    # Example text
    text = " KIT’S COLLEGE OF ENGINEERING IS THE BEST ENGINEERING COLLEGE IN MAHARASHTRA."
    # Preprocess the text
    words = preprocess_text(text)
    # Perform morphological analysis
    analyzed_words = perform_morphological_analysis(words)
    # Remove stop words
    final_words = remove_stop_words(analyzed_words)
    # Display the results
    print("Original Text:", text)
    print("Final Words:", final_words)
if __name__ == "__main__":
    main()
