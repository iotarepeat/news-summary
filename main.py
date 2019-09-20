from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
import string

stopWords = stopwords.words("english")
with open("input.txt") as f:
    input_text = f.read()

wordFrequency = Counter()
stem = PorterStemmer()
for word in word_tokenize(input_text):
    word = stem.stem(word).lower()
    if word not in stopWords:
        wordFrequency += Counter((word,))


def sentenceScore(sentence):
    score = 0
    sentence = sentence.lower()
    for word in word_tokenize(sentence):
        word = stem.stem(word)
        score += wordFrequency.get(word, 0)
    return score


N = 7
topN = sorted(sent_tokenize(input_text), key=sentenceScore, reverse=True)[:N]
for sentence in sent_tokenize(input_text):
    if sentence in topN:
        print(sentence)
        pass
