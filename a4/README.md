# anphilip-emkoby-p4

Part 1



Task: Create an inverted index and a document data file

What you'll before you run the code:

-> Python 2.7
-> BeautifulSoup 3
-> NLTK
-> A directory titled 'test_files' with two sub directories:
	1. Directory of html files
	2. index.dat file with format: name_of_html /tab url

Walking through an example: 
Let's use the given test files as an example.

First, run: python index.py YOURDIRECTORY/ index.dat. If you do not use this format, the code will not run and you will likely get an error message indicating that you did not put in the right arguments. You will get a sample input format in the error message. For us to read the document,  it is assumed that the html directory you provide will contain the necessary files as shown in the test documents. 

Using NLTK word_tokenize, all of the words are split up in the document into a list of strings. Then, remove the english stopwords provided by nltk from the tokenized list of words using list compression. Using NLTK PorterStemmer, stem each of the words in the resulting list. The final step is to update the inverted index dictionary by removing duplicates and setting a document ID.This is repeated for each document in the document directory if the document is also in the index.dat file. 

The next step is to create a document data dictionary. We will use a python package, BeautifulSoup to help parse the raw html text to retrieve the title. We decided to use BeatuifulSoup instead of simply regex becuase it is possible that multiple items other than title should be grabbed for the docs.dat file in the future. The title is pulled after the document is passed through BeautifulSoup and the resulting string, along with the document url and the length of the string is formatted into a dictionary. Again, this is repeated for each document in the document directory if the document is also in the index.dat file. 

Our final step is to write our dictionary to a file, and we decided to use a JSON object for writing to a file. This is because it makes it simpler to pull dictionaries back and forth from disk and memory using JSON objects to keep the integrity of the dictionary. The files will be written to disk where the program is run. 

Added features:
Testing capabilities, check if all arguments are passed in correctly and advise user, using BeautifulSoup and JSON objects keeping in mind future use.


Part 2
Task: Search the output from assignment 3 and part 1 of this assignment to find websites containing certain words

How we accomplished: stemmed/stopped the input words, selected a search mode. For or, accept any document containing that word. For and, select only files which have all of the words by checking per word searched. For most, use and but only require a 50% match.
Once you have matched, pull the url and title from docs.dat and total the number of files searched and the number of hits.

Walking through an example:
"python retreive.py or Appear William banister"
This outputs the files pulled from a sample scan of the CNN website which match to 7 different websites.

Hit URL: http://www.cnnnewsource.com/
Hit Title: CNN Newsource

Hit URL: http://www.cnnnewsource.com/contact/
Hit Title: Contact - CNN Newsource

Hit URL: http://www.cnnnewsource.com/classroom/
Hit Title: CNN Newsource - In the Classroom

Hit URL: http://www.cnnnewsource.com/latest-insights/
Hit Title: Latest Insights - CNN Newsource

Hit URL: http://www.cnnnewsource.com/cnn-collection/
Hit Title: CNN Collection - CNN Newsource

Hit URL: http://www.cnnnewsource.com/digital-services/
Hit Title: Digital Services - CNN Newsource

Hit URL: http://www.cnnnewsource.com/newsource/
Hit Title: Newsource - CNN Newsource

7 : Hits Count
8 : Total Searched Count

Added features: None
