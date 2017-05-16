import nltk
import re
import sys

class textInfo:
    '''
    Create instance of txtInfo class to get:
    - Number of words
    - Number of sentences
    - Total number of syllables
    - CL level
    - FK level
    
    Note: Make sure you have nltk installed on your machine
    We use the python nltk package to tokenize words 
    This is an effecient way to store words becuase 
    each word is associated with a token, for easy lookup
    
    Parameter:
    filename (str): text file (.txt extention) 
    
    Example:
    txt1 = textInfo(filename)
    '''

    def __init__(self, filename):
        '''
        Initialize:
        - filename
        - content of the file
        - create word tokens
        - word count
        '''
        self.filename = filename
        self.content_file = open(self.filename, 'r')
        self.content = self.content_file.read()
        self.tokens = nltk.word_tokenize(self.content)
        self.word_count = len(self.tokens)

    def getNumTitles(self):
        '''
        Find number of name titles in the file content
        '''
        ms = len(re.findall('\bMs.\b',self.content))
        mr = len(re.findall('\bMr.\b',self.content))
        dr = len(re.findall('\bDr.\b',self.content))
        mrs = len(re.findall('\bMrs.\b',self.content))
        
        numTitles = ms + mr + dr + mrs
        
        return numTitles

    def getSyllables(self):
    '''
        Find syllables in the document by the difference of
        dipthongs and vowel counts
    '''
        vowels = 'aeiouAEIOU'

        v_count = 0
        d_count = 0

        prev = False
        curr = False

        for letter in self.content:
            if letter in vowels:
                curr = True
                v_count += 1
            else:
                curr = False
            if prev and curr:
                d_count += 1

            prev = curr

        syl = v_count - d_count

        return syl

    def getSentences(self):
        '''
        Find number of sentences subtract number of name titles
        '''
        corpusReader = nltk.corpus.PlaintextCorpusReader('./',self.filename)
	return len(corpusReader.sents()) - self.getNumTitles()


    def getLetters(self):
        '''
        Get number of letters in the document
        '''
        return len(self.content)

    def clScore(self):
        '''
        Calculate CL Score
        '''
        return(5.88*(self.getLetters()/self.word_count) - 29.6*(self.getSentences()/self.word_count))

    def fkScore(self):
        '''
        Calculate FK Score
        '''
        return(0.39*(self.word_count/self.getSentences())+11.8*(self.getSyllables()/self.word_count))


def main():
    # get the filename from sys input
    file = sys.argv[1]
    txt1 = textInfo(file)

    print "Analyzing text document...."
    print "Number of words: {}".format(txt1.word_count)
    print "Number of sentences: {}".format(txt1.getSentences())
    print "CL level: {}".format(txt1.clScore())
    print "Total number of syllables: {}".format(txt1.getSyllables())
    print "FK level: {}".format(txt1.fkScore())

# run main
main()
