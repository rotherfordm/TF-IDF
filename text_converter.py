import pickle
from app.models import Article
from app import db
from .stopwordsremover import StopWordsRemover
from .texthandler import TextHandler
import json

def converted_text_update(input_journal):
	all_text = get_all_converted_text(input_journal)
	insert_converted_text_in_journal(all_text, input_journal)
	print("converted_text updated")

def get_all_converted_text(input_journal):
	pagetext = ''
	for pdf in input_journal.pdfs:
		pagetext = pagetext + ' ' + pdf.converted_text
	for page in input_journal.pages:
		pagetext = pagetext + ' ' + page.converted_text
	new_text = pagetext
	return new_text

def insert_converted_text_in_journal(text, input_journal):
	new_book = { 
	"ID" : int(input_journal.id),
	"Title" : input_journal.title.lower(),	
	"Subtitle" : input_journal.subtitle.lower(),
	"Author" : input_journal.author.lower(),
	"JournalTitle" : input_journal.journal_title.lower(),
	"PlaceOfPublisher" : input_journal.place_of_publisher.lower(),
	"NameOfPublisher" : input_journal.name_of_publisher.lower(),
	"ISSN" : input_journal.issn.lower(),
	"VolumeNumber" : input_journal.volume_number.lower(),
	"IssueNumber" : input_journal.issue_number.lower(),
	"YearOfPublication" : input_journal.year.lower(),
	"MonthOfPublication" : input_journal.month.lower(),
	"NoOfPages" : input_journal.no_of_pages.lower(),
	"Subject" : input_journal.subject.lower(),
	"RawText": text.lower(),
	"SanitizedText" : TextHandler().WordCounter(text.lower()),
	"RemovedStopWordsText": StopWordsRemover().remove(text.lower()),
	"TotalNoOfTerms" : len(text.lower().split(' ')),
	"TFIDF" : 0
	}
	indexfile = dict("")
	try:
		indexfile = TextHandler().OpenTextFrom("static", "index.JSON")
		indexfile = json.loads(indexfile)
	except Exception as ex:
		print(ex)
	print(input_journal.id)
	indexfile[int(input_journal.id)] = new_book
	TextHandler().SaveFileTo("static", "index.JSON", json.dumps(indexfile))
	db.session.add(input_journal)
	db.session.commit()

