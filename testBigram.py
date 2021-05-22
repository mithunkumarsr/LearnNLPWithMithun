import nltk

word_data = "Mithun is the biggest intellect in the world"
nltk_tokens = nltk.word_tokenize(word_data)

print(list(nltk.bigrams(nltk_tokens)))
