import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
nltk.download('all')

def get_semantic(seq, key_word):

      # Tokenization of the sequence
    temp = word_tokenize(seq)

    # Retrieving the definition
    # of the tokens
    temp = lesk(temp, key_word)
    return temp.definition()


keyword = 'book'
seq1 = 'I love reading books on coding.'
seq2 = 'The table was already booked by someone else.'

print(get_semantic(seq1, keyword))
print(get_semantic(seq2, keyword))

keyword = 'jam'
seq1 = 'My mother prepares very yummy jam.'
seq2 = 'Signal jammers are the reason for no signal.'

print(get_semantic(seq1, keyword))
print(get_semantic(seq2, keyword))
