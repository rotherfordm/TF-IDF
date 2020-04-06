import math
import re
from stemmer import Stemmer


class TFIDFHandler(object):

    # region Variables Getter - Setter

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = Stemmer.stem(value)  # Automatically Stem the input of the user

    @query.deleter
    def query(self):
        del self._query

    # endregion

    def calculate_tf(self, book_dict, term):
        """
        calculates the term frequency of a text in a text

        TF: Term Frequency, which measures how frequently a term occurs in a document. 
        Since every document is different in length, 
        it is possible that a term would appear much more times in long documents than shorter ones. 
        Thus, the term frequency is often divided by the document length 
        (aka. the total number of terms in the document) as a way of normalization: 

        TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)

        Parameters
        ----------
        arg1: Dictionary
            book dictionary
        arg2: String
            term
        Returns
        -------
        float
          term frequency of a term in a text
        """
        term_frequency = 0
        try:
            term_frequency = (
                book_dict["SanitizedText"][term] / book_dict["TotalNoOfTerms"]
            )
        except KeyError:
            print("Key Error, Term doesnt exist")
            return 0
        except ZeroDivisionError:
            print("tf division by zero!")
            return 0
        return term_frequency

    def calculate_idf(self, dict_of_books, term):
        """
        calculates the idf

        IDF: Inverse Document Frequency, which measures how important a term is. 
        While computing TF, all terms are considered equally important. 
        However it is known that certain terms, such as "is", "of", and "that",
        may appear a lot of times but have little importance. 
        Thus we need to weigh down the frequent terms while scale up the rare ones, 
        by computing the following: 

        IDF(t) = log_e(Total number of documents / Number of documents with term t in it)

        Parameters
        ----------
        arg1: Dictionary
            dictionary of books    
        arg2: String
            Term
        Returns
        -------
        float
          inverse document frequency
        """
        number_of_docs_with_term = 0
        for book_id in dict_of_books:
            try:
                dict_of_books[book_id]["SanitizedText"][term] is not KeyError
                number_of_docs_with_term = number_of_docs_with_term + 1
            except KeyError:
                print("term does not exist in this document")
        try:
            idf = math.log(len(dict_of_books) / number_of_docs_with_term)
            if idf == 0:
                return 1
            # print("idf: " +str(idf))
        except ZeroDivisionError:
            idf = 0
            print("idf division by zero!")
        return idf

    def calc_tfidf_per_book(self, dict_of_books):
        # print("\nTFIDF calculation:")
        new_dict_of_books = {}
        for book_id in dict_of_books:
            tf = self.calculate_tf(dict_of_books[book_id], self._query)
            idf = self.calculate_idf(dict_of_books, self._query)
            tfidf = tf * idf
            dict_of_books[book_id]["TFIDF"] = tfidf
            # print(dict_of_books.keys())
            if dict_of_books[book_id]["TFIDF"] != 0:
                new_dict_of_books[book_id] = dict_of_books[book_id]
            # print(str(dict_of_books[book_id]['ID']) +" "+ dict_of_books[book_id]['Title'] + " TF: " + str(tf) + " " + " IDF: " + str(idf) + " TFIDF: " + str(dict_of_books[book_id]['TFIDF']))
        # print("END calculation:")
        return new_dict_of_books

    def calc_total_tfidf_per_book(self, dict_of_books):
        print("\nTFIDF calculation:")
        new_dict_of_books = {}
        for book_id in dict_of_books:
            tf = self.calculate_tf(dict_of_books[book_id], self._query)
            idf = self.calculate_idf(dict_of_books, self._query)
            tfidf = tf * idf
            # print(str(tfidf) + 'tracer1')
            dict_of_books[book_id]["TFIDF"] = tfidf + dict_of_books[book_id]["TFIDF"]
            # print(str(dict_of_books[book_id]['TFIDF']) + 'tracer2')
            # print(dict_of_books.keys())
            if dict_of_books[book_id]["TFIDF"] != 0:
                new_dict_of_books[book_id] = dict_of_books[book_id]
            print(
                str(dict_of_books[book_id]["ID"])
                + " "
                + dict_of_books[book_id]["Title"]
                + " TF: "
                + str(tf)
                + " "
                + " IDF: "
                + str(idf)
                + " TFIDF: "
                + str(dict_of_books[book_id]["TFIDF"])
            )
        print("END calculation:")
        return new_dict_of_books

    def sort_by_tf_idf(self, dict_of_books):
        # print(sorted(dict_of_books, key=lambda x: (dict_of_books[x]['TFIDF']), reverse=True))
        return sorted(
            dict_of_books, key=lambda x: (dict_of_books[x]["TFIDF"]), reverse=True
        )
