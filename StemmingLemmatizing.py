from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer


porter = PorterStemmer()
snowball = SnowballStemmer(language="english")
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

word = "destabilize"
print(porter.stem(word))
print(snowball.stem(word))
print(lancaster.stem(word))
print("The lemmatized word is " + lemmatizer.lemmatize(word))

# list of tokenized words
words = ['cared', 'university', 'fairly', 'easily', 'singing','sings', 'sung', 'singer', 'sportingly']

# stem's of each word
stem_words = []
lemma_words = []
for w in words:
    x = snowball.stem(w)
    y = lemmatizer.lemmatize(w)
    stem_words.append(x)
    lemma_words.append(y)

# print stemming results
for e1, e2, e3 in zip(words, stem_words, lemma_words):
    print(e1+' --stemming--> '+e2+' --lemmatizing--> '+e3)
