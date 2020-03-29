import nltk
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer("english")
 
class Stemmer(object):

	def stem(self, text):
		textAux = []
		tokenAux = []  # we declare list for storing tokens
		tokens = nltk.word_tokenize(text)
		for token in tokens:
			tokenAux = token
			tokenAux = snowball_stemmer.stem(token)    
			textAux.append(tokenAux)  # we add new token into the resulting list
		result = " ".join(textAux)  # join list using space as separator
		return(result)	

