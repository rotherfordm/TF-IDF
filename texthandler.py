from collections import Counter
import json
from textsanitizer import TextSanitizer


class TextHandler(object):
    @staticmethod
    def WordCounter(text):
        return Counter(text.split())

    def SaveFileTo(self, destination, filename, x):
        with open(destination + "\\" + filename, "w") as outfile:
            json.dump(x, outfile)
            print("Saved!")

    def OpenTextFrom(self, file_location, filename):
        with open(file_location + "\\" + filename) as json_file:
            json_data = json.load(json_file)
            return json_data
