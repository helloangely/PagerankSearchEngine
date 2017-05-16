# imports
import sys, ast, math
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# retrieves documents
def retrieve(words):

    # remove stopwords
    gowords = bye_stopwords(words)

    # apply stemmer
    stemmed = stemmer(gowords)

    retrieve_most(stemmed)

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

# most search
def retrieve_most(stemmed):
    inv_index = {}
    matched_init = []
    matched_final = []
    docs_dat = {}
    # makes dictionary from invindex
    with open("invindex.dat", "r") as invfile:
        inv_index = ast.literal_eval(invfile.read())
    # searches for word in invindex and appends matches to list
    for word in stemmed:
        try:
            for item in inv_index[word]:
                matched_init.append(item)
        except:
            pass

    # removes items/documents with less iterations than half the amount of words searched
    for item in matched_init:
        if matched_init.count(item) > (len(stemmed) / 2.0):
            matched_final.append(item)
            matched_init.remove(item)

    with open("docs.dat", "r") as docs:
        docs_dat = ast.literal_eval(docs.read())

    # Calculate TF
    for item in matched_final:
        tf_score = float(item[1]) / docs_dat[item[0]][2]
        item = item.append(tf_score)

    # Calculate IDF
    idf = math.log(len(docs_dat)/len(matched_final))

    # Calculate TF-IDF
    for item in matched_final:
        tf_idf_score = item[2] * idf
        item[2] = tf_idf_score

    # Print results
    for item in matched_final:
        print "Hit URL:", docs_dat[item[0]][0]
        print "Hit Title:", docs_dat[item[0]][1]
        print "TF-IDF:", item[2]
        print

# main
def main():
    if len(sys.argv) >= 2:
        retrieve(sys.argv[1:])
    else:
        print "Too many or too few arguments. Try 'python retrieve2.py word1 word2 word3 ...'"

main()
