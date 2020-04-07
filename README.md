# TF-IDF - Term frequency-inverse document frequency implmentation

Tf-idf stands for _term frequency-inverse document frequency_, and the tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus. Variations of the tf-idf weighting scheme are often used by search engines as a central tool in scoring and ranking a document's relevance given a user query.

One of the simplest ranking functions is computed by summing the tf-idf for each query term; many more sophisticated ranking functions are variants of this simple model.

Tf-idf can be successfully used for stop-words filtering in various subject fields including text summarization and classification.

This module is implmented in Python.

## Table of Contents

1.  [Built With](https://github.com/HeatzRM/TF-IDF#built-with)
2.  [Installation](https://github.com/HeatzRM/TF-IDF#installation)
3.  [Examples](https://github.com/HeatzRM/TF-IDF#examples)
4.  [References](https://github.com/HeatzRM/TF-IDF#references)

## Built With

- [Python](https://www.python.org/) - The programming language used
- [NLTK](https://pypi.org/project/nltk/) - Natural Language Toolkit (NLTK)
- [Travis CI](https://travis-ci.com/) - Continuous Integration service

## Installation

```
pip install virtualenv
```

Make virtual environment

```
virtualenv venv
```

Enter virtual environment

```
#Windows
venv\Scripts\activate

#Linux
source venv/bin/activate
```

Install packages

```
pip install -r requirements.txt
```

## Examples

Full test: [test.py](https://github.com/HeatzRM/TF-IDF/blob/master/test.py)

```
from stopwordsremover import StopWordsRemover
from texthandler import TextHandler
from stemmer import Stemmer
from tfidf import TFIDFHandler
from searchhandler import SearchHandler

text2 =  """
Artificial neural networks (ANN) or connectionist systems are computing systems
vaguely inspired by the biological neural networks that constitute animal brains.
Such systems "learn" to perform tasks by considering examples, generally without
being programmed with task-specific rules. For example, in image recognition,
they might learn to identify images that contain cats by analyzing example images
that have been manually labeled as "cat" or "no cat" and using the results to
identify cats in other images. They do this without any prior knowledge of cats,
for example, that they have fur, tails, whiskers and cat-like faces. Instead,
they automatically generate identifying characteristics from the examples that
they process.
"""

# Remove Stopwords or unnessary words such as is, a, and
removed_stopwords_text = StopWordsRemover.remove(text)

# Stem to reduce inflected words to their word stem, base or root form
stemmed_text = Stemmer.stem(removed_stopwords_text)

# Counts number of words has appeared in the document
sanitized_text = TextHandler.WordCounter(stemmed_text)

book =  {
"ID":  '1',
"Title":  "Artificial neural network",
"Subtitle":  "neural networks",
"Author":  "author 1",
"RawText": text1,
"SanitizedText": sanitized_text1,
"RemovedStopWordsText": removed_stopwords_text1,
"TotalNoOfTerms":  len(text.lower().split("  ")),
"TFIDF":  0,
}
```

```
tfIDFHandler =  TFIDFHandler()
books =  {'1': book}
tfIDFHandler.query =  "neural"
tfIDFHandler.calc_total_tfidf_per_book(books)
print("tfIDFHandler.query",  "neural")
```

```
TFIDF calculation:
1 Artificial neural network TF: 0.018691588785046728  IDF: 1 TFIDF: 0.018691588785046728
END calculation:
tfIDFHandler.query neural
```

## References

[tfidf](http://www.tfidf.com/) - tfidf.com
