import sys
import numpy

class training:
	def __init__(self, doc_name):
		self.doc_name = doc_name
		
	def training(self, doc_name):
		
		doc_words = get_words_from_doc("entertainment")
		
		
	def get_words_from_doc(self, doc):
		all_words = []
		all_words.append(doc.words)
		freq_words = nltk.FreqDist(all_words)
		word_features = list(freq_words)
		
		return set(word_features)
		
        
        
	

class documentClass:

    def __init__(self, filename):
        self.filename = filename
        self.content_file = open(self.filename, 'r')
        self.content = self.content_file.read()
		
    
    def classify(self):
        return


def main():
  file = sys.argv[1]
  classifier1 = documentClass(file)

  print("Score for category: ")
  print("- business: ")
  print("- entertainment: ")
  print("- tech: ")
  print("- sports: ")
  print("- politics: ")

main()
