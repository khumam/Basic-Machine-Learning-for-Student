from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()


def stemString(string):
    output = stemmer.stem(string)
    return output
