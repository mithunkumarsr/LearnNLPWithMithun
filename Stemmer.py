from nltk.stem import PorterStemmer, lancaster
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer

porter = PorterStemmer()
snowball = SnowballStemmer(language="english")
lancaster = LancasterStemmer()

word = "destabilize"
print(porter.stem(word))
print(snowball.stem(word))
print(lancaster.stem(word))

# list of tokenized words
words = ['cared', 'university', 'fairly', 'easily', 'singing',
         'sings', 'sung', 'singer', 'sportingly']

# stem's of each word
stem_words = []
for w in words:
    x = snowball.stem(w)
    stem_words.append(x)

# print stemming results
for e1, e2 in zip(words, stem_words):
    print(e1+' ----> '+e2)
