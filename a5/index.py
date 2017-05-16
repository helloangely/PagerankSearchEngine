# imports
import sys
import re
import json
from BeautifulSoup import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from os import listdir

# indexing
def index(html_directory, index_dat):

    # initialize inverted index
    inverted_index = {}
    doc_id = ""
    d = format_index_dat(index_dat)
    docs_dat = {}

    for document in listdir(html_directory):
        doc_id = document
        if html_directory + document in d:
            # read file
            raw_file = open(html_directory  + document, "r")
            raw_content = unicode(raw_file.read(), errors='replace')
            raw_file.close()

            # tokenize file contents
            tokenized = word_tokenize(raw_content)

            # remove stopwords
            gowords = bye_stopwords(tokenized)

            # apply stemmer
            stemmed = stemmer(gowords)

            # update inverted index
            update_inverted_index(stemmed, inverted_index, doc_id)

            # get length of html doc
            len_document = len(tokenized)

            # get the title of the html doc 
            title_html = get_title_html(raw_content)

            # get URL of the document 
            doc_url = d[html_directory  + document].rstrip("\n")

            # update docs dat dictionary 
            update_docs_dat_dict(docs_dat,document,len_document,title_html,doc_url)

        else:
            print document + " ignored becuase it is not in the index.dat file."

    # write inverted index and docs info to disk 
    write_to_file(inverted_index, "invindex.dat")
    write_to_file(docs_dat, "docs.dat")

    return inverted_index

        
def bye_stopwords(tokenized_list):
    stop_words = stopwords.words('english')
    gowords = [w for w in tokenized_list if not w in stop_words]
    gowords=[]
    for w in tokenized_list:
        if w not in stop_words:
            gowords.append(w)
        
    return gowords

def stemmer(gowords):
    ps = PorterStemmer()
    stemmed_list = []
    for w in gowords:
        stemmed_list.append(ps.stem(w))
    return stemmed_list

def update_inverted_index(stemmed_words, inverted_index, doc_id):

    # make tuples for words and doc ids
    word_list = []
    
    for word in stemmed_words:
        word_count = stemmed_words.count(word)
        word_list.append((word,doc_id,word_count))

    # remove duplicates from word_list
    word_list = list(set(word_list))

    # update the inverted index
    for k in word_list:
        if k[0] in inverted_index and inverted_index.get(k[0], None) is not None:
            if k[1] not in inverted_index[k[0]]:
                inverted_index[k[0]].append([k[1],k[2]])
        else:
            inverted_index.update({k[0]:[[k[1],k[2]]]})
    

def format_index_dat(index_dat):
    # check if html directory doc is in the index file
    with open(index_dat) as fin:
        rows = ( line.split('\t') for line in fin )
        d = { row[0]:row[1] for row in rows }
    return d

def get_title_html(html_txt):
    soup = BeautifulSoup(html_txt)
    title = soup.title.string
    return title

def write_to_file(dict_data, filename):
    # write dictionary to file using json object
    with open(filename, 'w') as f:
        json.dump(dict_data, f)

def update_docs_dat_dict(docs_dat,document,len_document,title_html,doc_url):
    docs_dat.update({document:[doc_url, title_html, len_document]})


# main
def main():
    if len(sys.argv) == 3:
        index(sys.argv[1], sys.argv[2])
    else:
        print "Too many or too few arguments. Try 'python index.py your_html_directory index.dat'"

main()







