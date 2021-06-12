import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer


sent = "The little mouse ate the fresh cheese"
print(nltk.pos_tag(word_tokenize("singing")))
sent_tokens = nltk.pos_tag(word_tokenize(sent))
grammar_np = r"NP:{<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar_np)
chunk_result = chunk_parser.parse(sent_tokens)
print(chunk_result)


sent2 = "She is walking quickly to the mall"
sent2_tokens = nltk.pos_tag(word_tokenize(sent2))
grammar_np2 = r"VP:{<PRP>?<VB|VBD|VBZ|VBG>*<RB|RBR>?}"
chunk2_parser = nltk.RegexpParser(grammar_np2)
chunk2_result = chunk2_parser.parse(sent2_tokens)
print(chunk2_result)
