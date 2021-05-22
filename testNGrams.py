from nltk import ngrams

sentence = 'this is a foo bar sentences and i want to ngramize it'

n = 1
myNGrams = ngrams(sentence.split(), n)

for grams in myNGrams:
    print grams
