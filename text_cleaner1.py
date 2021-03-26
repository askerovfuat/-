from alphabet_detector import AlphabetDetector
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist

ad = AlphabetDetector()


with open("D:/python_arcticles/texts1.txt", 'r') as f:
    words = [line.rstrip('\n') for line in f]


def is_there_number(string):
    return any(i.isdigit() for i in string)


def is_not_blank(s):
    return bool(s and s.strip())


nltk.download('stopwords')
mywords = []

for word in words:
    if ad.only_alphabet_chars(u"{}".format(word), "CYRILLIC") and is_there_number(word) == False \
            and is_not_blank(word) and word not in stopwords.words('russian'):
        mywords.append(word)
print(mywords)

fdist = FreqDist(mywords)

print(fdist.most_common(5))
