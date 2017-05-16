For the second part of the assignment, we were given the task to classify a given document. 
This task can be split up into two key parts: training and classifying. 
We need to train our program to understand what a document classification really means. 
In this sense, we set of pre-selected documents that fit into certain classifications. 
An example would be a health file would be taken in for the health category and our program would learn all of the words in that category and associate those key elements with the health category. 
Our code works by computing the score of each corpora for the document, by going word by word, finding the ni and n-i values, and capturing their subtraction in a list.
This list is used to pass the score of each corpora by summing all the word's scores.
The list can also be used to sort these scores and find a best matched category.
Finally, the list can find the top five contributing positive words by sorting the list's internal word score dictionary/list.
One struggle we faced for this project was the contribution to the score of punctuation.
We also suffered from incompatibility between utf8 and unicode texts.
As a result, we deigned to remove punctuation in calculating word score.
This solved our issue of confusing between business and other categories overtaking by having more puntuation.
We also uncapitalized all words to remove the seperation of title capped and lower cased words.

The testing results were reasonable. We used the given tests.