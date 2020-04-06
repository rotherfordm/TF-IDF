from stopwordsremover import StopWordsRemover
from texthandler import TextHandler
from stemmer import Stemmer

# Text to be converted
text =  '''
The 2019–20 coronavirus pandemic is an ongoing pandemic of coronavirus disease 2019 (COVID-19), caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).[6][b] The outbreak was first noted in Wuhan, Hubei province, China, in December 2019. The World Health Organization (WHO) declared the outbreak to be a Public Health Emergency of International Concern on 30 January 2020 and recognized it as a pandemic on 11 March 2020.[8][9] As of 6 April 2020, more than 1,270,000 cases of COVID-19 have been reported in over 200 countries and territories,[5] resulting in approximately 69,400 deaths.[4] More than 260,000 people have recovered.
'''

# Remove Stopwords or unnessary words such as is, a, and 
removed_stopwords_text = StopWordsRemover.remove(text)

# Stem to reduce inflected words to their word stem, base or root form
stemmed_text = Stemmer.stem(removed_stopwords_text)

# Counts number of words has appeared in the document
counted_text = TextHandler.WordCounter(stemmed_text)



print(counted_text)