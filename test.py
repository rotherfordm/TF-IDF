from stopwordsremover import StopWordsRemover
from texthandler import TextHandler
from stemmer import Stemmer
from tfidf import TFIDFHandler


# Text to be converted
text = """
The 2019–20 coronavirus pandemic is an ongoing pandemic of coronavirus disease 2019 (COVID-19), caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The outbreak was first noted in Wuhan, Hubei province, China, in December 2019. The World Health Organization (WHO) declared the outbreak to be a Public Health Emergency of International Concern on 30 January 2020 and recognized it as a pandemic on 11 March 2020. As of 6 April 2020, more than 1,270,000 cases of COVID-19 have been reported in over 200 countries and territories, resulting in approximately 69,400 deaths. More than 260,000 people have recovered.
"""
# Remove Stopwords or unnessary words such as is, a, and
removed_stopwords_text = StopWordsRemover.remove(text)
# Stem to reduce inflected words to their word stem, base or root form
stemmed_text = Stemmer.stem(removed_stopwords_text)
# Counts number of words has appeared in the document
sanitized_text = TextHandler.WordCounter(stemmed_text)
# print(sanitized_text)
book1 = {
    "ID": 1,
    "Title": "Covid",
    "RawText": text,
    "SanitizedText": sanitized_text,
    "RemovedStopWordsText": removed_stopwords_text,
    "TotalNoOfTerms": len(text.lower().split(" ")),
    "TFIDF": 0,
}

text2 = """
Artificial neural networks (ANN) or connectionist systems are computing systems vaguely inspired by the biological neural networks that constitute animal brains. Such systems "learn" to perform tasks by considering examples, generally without being programmed with task-specific rules. For example, in image recognition, they might learn to identify images that contain cats by analyzing example images that have been manually labeled as "cat" or "no cat" and using the results to identify cats in other images. They do this without any prior knowledge of cats, for example, that they have fur, tails, whiskers and cat-like faces. Instead, they automatically generate identifying characteristics from the examples that they process.
"""
# Remove Stopwords or unnessary words such as is, a, and
removed_stopwords_text2 = StopWordsRemover.remove(text2)
# Stem to reduce inflected words to their word stem, base or root form
stemmed_text2 = Stemmer.stem(removed_stopwords_text2)
# Counts number of words has appeared in the document
sanitized_text2 = TextHandler.WordCounter(stemmed_text2)
# print(sanitized_text)
book2 = {
    "ID": 2,
    "Title": "Artificial neural network",
    "RawText": text2,
    "SanitizedText": sanitized_text2,
    "RemovedStopWordsText": removed_stopwords_text2,
    "TotalNoOfTerms": len(text2.lower().split(" ")),
    "TFIDF": 0,
}

text3 = """
A bioreactor refers to any manufactured device or system that supports a biologically active environment. In one case, a bioreactor is a vessel in which a chemical process is carried out which involves organisms or biochemically active substances derived from such organisms. This process can either be aerobic or anaerobic. These bioreactors are commonly cylindrical, ranging in size from litres to cubic metres, and are often made of stainless steel.

It may also refer to a device or system designed to grow cells or tissues in the context of cell culture. These devices are being developed for use in tissue engineering or biochemical/bioprocess engineering.
"""
# Remove Stopwords or unnessary words such as is, a, and
removed_stopwords_text3 = StopWordsRemover.remove(text3)
# Stem to reduce inflected words to their word stem, base or root form
stemmed_text3 = Stemmer.stem(removed_stopwords_text3)
# Counts number of words has appeared in the document
sanitized_text3 = TextHandler.WordCounter(stemmed_text3)
# print(sanitized_text)
book3 = {
    "ID": 3,
    "Title": "Bioreactor",
    "RawText": text3,
    "SanitizedText": sanitized_text3,
    "RemovedStopWordsText": removed_stopwords_text3,
    "TotalNoOfTerms": len(text3.lower().split(" ")),
    "TFIDF": 0,
}


tfIDFHandler = TFIDFHandler()

tfIDFHandler.query = "coronavirus"
tfIDFHandler.calc_total_tfidf_per_book({1: book1, 2: book2, 3: book3})
print("tfIDFHandler.query", "coronavirus")

tfIDFHandler.query = "neural"
tfIDFHandler.calc_total_tfidf_per_book({1: book1, 2: book2, 3: book3})
print("tfIDFHandler.query", "neural")

tfIDFHandler.query = "bioreactor"
tfIDFHandler.calc_total_tfidf_per_book({1: book1, 2: book2, 3: book3})
print("tfIDFHandler.query", "bioreactor")
