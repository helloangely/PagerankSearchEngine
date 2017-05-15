import sys
import re
import json
from BeautifulSoup import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
import errno
from collections import Counter


class Index:
    def __init__(self, from_dir, index_data):
        self.from_dir = from_dir
        self.directory = os.path.join(os.getcwd(), from_dir)
        self.index_data = self.from_dir + "\\" + index_data
        self.formatted_index = self.format_index_dat()
        self.invindex = {}
        self.docs = {}

    def generate_data_structures(self):
        self.clean_html_directory()
        self.write_to_file(self.invindex, "invindex.dat")
        self.write_to_file(self.docs, "docs.dat")
    
    def clean_html_directory(self):
        if os.path.isdir(self.directory):
            for document in os.listdir(self.directory):
                self.clean_file(document)
        else:
            print "Invalid directory for reading html files in indexer!"

    def clean_file(self, document):
        doc_id = document
        if self.from_dir + document in self.formatted_index:
            raw_file = open(self.directory + "/" + document, "r")
            raw_content = unicode(raw_file.read(), errors='replace')
            raw_file.close()

            # tokenize file contents
            tokenized = word_tokenize(raw_content)

            # remove stopwords
            gowords = self.bye_stopwords(tokenized)

            # apply stemmer
            stemmed = self.stemmer(gowords)

            # update inverted index
            self.update_inverted_index(stemmed, doc_id)

             # get length of html doc
            len_document = len(tokenized)

            html_info = self.get_links_html(raw_content)
            
            # get outward links 
            links_html = html_info[0]

            # get the title of the html doc 
            title_html = html_info[1]

            # get URL of the document
            doc_url = self.formatted_index[self.from_dir + document].strip()

            # update docs dat dictionary 
            self.update_docs_dat_dict(document,len_document,links_html,doc_url,title_html)
            
        elif document == "index.dat":
            pass
        else:
            print document + " ignored because it is not in the index.dat file."

    def format_index_dat(self):
        index_dat = self.index_data
        # check if html directory doc is in the index file
        with open(index_dat) as fin:
            rows = ( line.split('\t') for line in fin )
            d = { row[0]:row[1] for row in rows }
        return d

    def bye_stopwords(self, tokenized_list):
        stop_words = stopwords.words('english')
        gowords=[]
        for w in tokenized_list:
            if w not in stop_words:
                gowords.append(w)
        return gowords

    def stemmer(self, gowords):
        ps = PorterStemmer()
        stemmed_list = []
        for w in gowords:
            stemmed_list.append(ps.stem(w))
        return stemmed_list

    def update_inverted_index(self, stemmed_words, doc_id):

        # make tuples for words and doc ids
        word_list = []

        cnt = Counter()
        for word in stemmed_words:
            cnt[word] += 1
        for word in cnt:
            word_list.append((word,doc_id,cnt[word]))

        # remove duplicates from word_list
        word_list = list(set(word_list))

        # update the inverted index
        for k in word_list:
            if k[0] in self.invindex and self.invindex.get(k[0], None) is not None:
                if k[1] not in self.invindex[k[0]]:
                    self.invindex[k[0]].append([k[1],k[2]])
            else:
                self.invindex.update({k[0]:[[k[1],k[2]]]})

    def get_links_html(self, html_txt):
        soup = BeautifulSoup(html_txt)
        links = []
        for link in soup.findAll('a'):
            if link.get('href'):
                links.append(link.get('href'))
        title = soup.title.string
        return links, title

    def write_to_file(self, dict_data, filename):
        # write dictionary to file using json object
        with open(filename, 'w') as f:
            json.dump(dict_data, f)

    def update_docs_dat_dict(self,document,len_document,links_html,doc_url,title_html):
        self.docs.update({document:[doc_url, len_document, links_html, title_html]})

def main():
    if len(sys.argv) < 3:
        print 'Not enough arguments!'
        return
    from_dir = sys.argv[1]
    index_data = sys.argv[2]
    index = Index(from_dir, index_data)
    index.generate_data_structures()
main()
