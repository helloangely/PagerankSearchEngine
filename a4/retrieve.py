# imports
import sys
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import ast

# retrieves documents
def retrieve(mode, words):

    # remove stopwords
    gowords = bye_stopwords(words)

    # apply stemmer
    stemmed = stemmer(gowords)

    # pick function from mode
    if mode == "or":
        retrieve_or(stemmed)
    elif mode == "and":
        retrieve_and(stemmed)
    elif mode == "most":
        retrieve_most(stemmed)
    else:
        print "Mode submitted not valid!"

# removes stopwords
def bye_stopwords(tokenized_list):
    stop_words = stopwords.words('english')
    gowords = [w for w in tokenized_list if not w in stop_words]
    gowords=[]
    for w in tokenized_list:
        if w not in stop_words:
            gowords.append(w) 
    return gowords

# stems words
def stemmer(gowords):
    ps = PorterStemmer()
    stemmed_list = []
    for w in gowords:
        stemmed_list.append(ps.stem(w))
    return stemmed_list

# or search
def retrieve_or(stemmed):
    inv_index = {}
    matched = []
    docs_dat = {}
    # makes dictionary from invindex
    with open("invindex.dat", "r") as invfile:
        inv_index = ast.literal_eval(invfile.read())
    # searches for word in invindex and appends matches to list
    for word in stemmed:
        try:
            for item in inv_index[word]:
                if item not in matched:
                    matched.append(item)
        except:
            pass
    # counts documents searched through
    with open("docs.dat", "r") as docs:
        docs_dat = ast.literal_eval(docs.read())
    for item in matched:
        print "Hit URL:", docs_dat[item[0]][0]
        print "Hit Title:", docs_dat[item[0]][1]
        print
    print str(len(matched)), ": Hits Count\n", str(len(docs_dat)), ": Total Searched Count"

# and search
def retrieve_and(stemmed):
    inv_index = {}
    matched_init = []
    matched_final = []
    docs_dat = {}
    marker = 0
    # makes dictionary from invindex
    with open("invindex.dat", "r") as invfile:
        inv_index = ast.literal_eval(invfile.read())
    # searches for word in invindex and appends matches to list
    for word in stemmed:
        try:
            for item in inv_index[word]:
                if item in matched_init:
                    pass
                else:
                    matched_init.append(item)
                marker += 1
        except:
            pass
    # removes items/documents with less iterations than the amount of words searched
    for item in matched_init:
        if matched_init.count(item) == len(stemmed):
            matched_final.append(item)
        else:
            matched_init.remove(item)
            
    # counts documents searched through
    with open("docs.dat", "r") as docs:
        docs_dat = ast.literal_eval(docs.read())
    for item in matched_final:
        print "Hit URL:", docs_dat[item[0]][0]
        print "Hit Title:", docs_dat[item[0]][1]
        print
    print str(len(matched_final)), ": Hits Count\n", str(len(docs_dat)), ": Total Searched Count"

# most search
def retrieve_most(stemmed):
    inv_index = {}
    matched_init = []
    matched_final = []
    docs_dat = {}
    marker = 0
    # makes dictionary from invindex
    with open("invindex.dat", "r") as invfile:
        inv_index = ast.literal_eval(invfile.read())
    # searches for word in invindex and appends matches to list
    for word in stemmed:
        try:
            for item in inv_index[word]:
                if item in matched_init:
                    pass
                else:
                    matched_init.append(item)
                marker += 1
        except:
            pass
    # removes items/documents with less iterations than the amount of words searched
    for item in matched_init:
        if matched_init.count(item) > (len(stemmed) / 2):
            matched_final.append(item)
        else:
            matched_init.remove(item)
            
    # counts documents searched through
    with open("docs.dat", "r") as docs:
        docs_dat = ast.literal_eval(docs.read())
    for item in matched_final:
        print "Hit URL:", docs_dat[item[0]][0]
        print "Hit Title:", docs_dat[item[0]][1]
        print
    print str(len(matched_final)), ": Hits Count\n", str(len(docs_dat)), ": Total Searched Count"

# main
def main():
    if len(sys.argv) >= 3:
        retrieve(sys.argv[1], sys.argv[2:])
    else:
        print "Too many or too few arguments. Try 'python retrieve.py mode word1 word2 word3 ...'"

main()
