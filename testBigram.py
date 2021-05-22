import nltk

word_data = "INDIA is the 7th largest country in the world"
nltk_tokens = nltk.word_tokenize(word_data)

print(list(nltk.bigrams(nltk_tokens)))
