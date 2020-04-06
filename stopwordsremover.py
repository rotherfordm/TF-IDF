from nltk.corpus import stopwords
import re


class StopWordsRemover(object):
    @staticmethod
    def remove(text):
        """
        converts the text into a list of text and 
        removes the stopwords in the input_text
        and returns the new text as text  
        """
        word_list = re.sub("[^\w]", " ", text).split()
        filtered_words = [
            word for word in word_list if word not in stopwords.words("english")
        ]
        new_text = " ".join(filtered_words)
        return new_text
