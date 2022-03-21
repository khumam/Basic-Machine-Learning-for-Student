import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()
removeFactory = StopWordRemoverFactory()
stopword = removeFactory.create_stop_word_remover()


def stemString(string):
    output = stemmer.stem(string)
    return output


def removeStopWord(string):
    return stopword.remove(string)


def cleanString(string):
    return re.sub('[\W_]|(URL)|(USERNAME)', ' ', string)
