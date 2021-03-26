import string
import re
import json

news = open('D:/python_arcticles/texts.txt', 'rt')
news_text = news.read()

words = news_text.split()

punct = "!#$%&'()*+, -./:<= >?@[\] ^ _`{ | }~«»№—–"

table = str.maketrans('', '', punct)

words_stripped = [w.translate(table) for w in words]


def string_contain_number(string):
    return bool(re.search(r'\d', string))


for word in words_stripped:
    if string_contain_number(word) == True or word == '':
        words_stripped.remove(word)

with open('D:/python_arcticles/texts1.txt', 'w') as f:
    f.write("\n".join(words_stripped))
