import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import udhr
from urllib import request
from nltk.probability import FreqDist

languages = ['Afrikaans', 'Danish', 'Dutch', 'English', 'German', 'Indonesian',
'Italian','Spanish', 'Swedish']

utf_languages = [i for i in udhr.fileids() if i[-5:] == '-UTF8']
print(utf_languages)
fdist = FreqDist(udhr.words(utf_languages[10]))
