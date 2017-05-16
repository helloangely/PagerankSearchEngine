import math, sys

# Uses lists to determine corpora to load, and the n-i score for each through excluded items in each list. Saves computing power.
corpora = ["business", "entertainment", "health", "scitech", "sports", "world"]
corpora_list = [["entertainment", "health", "scitech", "sports", "world"],
["business", "health", "scitech", "sports", "world"],
["business", "entertainment", "scitech", "sports", "world"],
["business", "entertainment", "health", "sports", "world"],
["business", "entertainment", "health", "scitech", "world"],
["business", "entertainment", "health", "scitech", "sports"]]

# Calculates the score change per word passed in by determining ni and n-i for passed words.
def score_change(word, category):
        ni = 1
        n_i = 1
        if category == "business":
                new_corpora = corpora_list[0]
        elif category == "entertainment":
                new_corpora = corpora_list[1]
        elif category == "health":
                new_corpora = corpora_list[2]
        elif category == "scitech":
                new_corpora = corpora_list[3]
        elif category == "sports":
                new_corpora = corpora_list[4]
        elif category == "world":
                new_corpora = corpora_list[5]
        try:
                for wordd in open(category, "r").read():
                        if wordd == word:
                                ni += 1

                for corpus in new_corpora:
                        for wordd in open(corpus, "r").read():
                                if wordd == word:
                                        n_i += 1
        except:
                print "Issues finding corpora files or files in wrong format/of wrong type. Please try again."

        score = math.log(ni) - math.log(n_i)
        return score      

# Takes a given document and category and returns the category, score and list of scores per word for that document in that category.
def scoremaker(document, category):
        score = 0
        scoredict = {}
        try:
                document = open(document, "r")
                document = document.read()
                document = document.split(" ")
        except:
                print "Document passed is inappropriate filetype or format for this program. Please try again."
        for word in document:
                word = word.lower()
                if (word in "!.?,"):
                        pass
                else:
                        change = score_change(word, category)
                        score += change
                        scoredict[change] = word
        score = [category, score, scoredict]
        return score

# Reads the command line argument and attempts to start evaluating
item = sys.argv[1]
scores = []
high_score = []
print "Evaluating the " + item + "..."

# Runs scoremaker for each corpus and adds the output to a list
for i in corpora:
        scores.append(scoremaker(item, i))

# Prints the scores in the list for every corpus, puts the highest category in high_score replacing it when it is beaten
print "Score for category:"
for i in scores:
        print "\t- " + str(i[0]) + ":\t\t" + str(i[1])
        if high_score:
                if high_score[1] < i[1]:
                        high_score = i
        else:
                high_score = i
                
print
print
print "The document's category is most likely:\t" + high_score[0]
print
print "The most informative words in this document were:"

# Takes the high score's words and sorts them by highest positive contributor to the overall score (or least negative)
informative = sorted(high_score[2].items())
for i in range(5):
        print "\t- " + str(informative[i][0]) + "\t\t" + str(informative[i][1])
        

