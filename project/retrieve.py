# imports
import sys, ast, math
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class Retriever():
    def __init__(self, words):
        self.words = words
        self.gowords = self.bye_stopwords(self.words)
        self.stemmed = self.stemmer(self.gowords)
        self.tf_idf_dict = self.retrieve_most(self.stemmed)

    # removes stopwords
    def bye_stopwords(self, tokenized_list):
        stop_words = stopwords.words('english')
        gowords = [w for w in tokenized_list if not w in stop_words]
        gowords=[]
        for w in tokenized_list:
            if w not in stop_words:
                gowords.append(w) 
        return gowords

    # stems words
    def stemmer(self, gowords):
        ps = PorterStemmer()
        stemmed_list = []
        for w in gowords:
            stemmed_list.append(ps.stem(w))
        return stemmed_list

    # most search
    def retrieve_most(self, stemmed):
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

        for i in matched_init:
            if i not in matched_final:
                matched_final.append(i)

        if(len(matched_final) <= 0):
            print "No matches!"
        else:
            with open("docs.dat", "r") as docs:
                docs_dat = ast.literal_eval(docs.read())

            # Calculate TF
            for item in matched_final:
                tf_score = float(item[1]) / docs_dat[item[0]][1]
                item = item.append(tf_score)

            # Calculate IDF
            idf = math.log((len(docs_dat)/len(matched_final)) + 10)

            # Calculate TF-IDF
            for item in matched_final:
                tf_idf_score = item[2] * idf
                item[2] = tf_idf_score

            tfidf_dict = {}
            # Return results
            for item in matched_final:
                tfidf_dict[docs_dat[item[0]][0]] = item[2], item[0], docs_dat[item[0]][3]
            return tfidf_dict

# main
def main():
    if len(sys.argv) >= 2:
        retrieve = Retriever(sys.argv[1:])
    else:
        pass
main()




