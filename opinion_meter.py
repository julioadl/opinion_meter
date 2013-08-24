import numpy as np
import csv as csv
import math
import sys

#open dictionary

afinfile = open(sys.argv[1])

# open and import into the CSV. It skips the first line as it's the header
csv_file_object = csv.reader(open(sys.argv[2], "rb"))
header = csv_file_object.next()
data = []

#fill the data into a list
for row in csv_file_object:
    data.append(row)

#transforms data into an array
data = np.array(data)

#new list that contains tuples of (id, string)
#question key: question1b
question = {}
for individual in range(len(data)):
    response = []
    response.append(data[individual,17])    #picks up the item of the numpy array
    response.append(data[individual,18])
    response.append(data[individual,19])
    response.append(data[individual,20])
    question[data[individual,0]] = response #adds the items of the numpy array into one individual respone

#new dictionary
dictionary = []
negatives = ['no', 'No', 'NO', 'Nothing', 'nothing', 'none', 'None','NONE']
neutrals = ['Nothing', 'nothing']

for line in afinfile:
    dictionary.append(line)

#scores
scores = {}
for item in dictionary:
    term, score = item.split()
    #term = term.decode('utf-8')
    scores[term] = int(score)

#compare with dictionary
for individual in question:
    general_score = 0
    
    for answer in question[individual]:
        score_feeling = 0
        words = answer.split()

        for term in scores:
            for item in words: 
                if term == item:
                    score_feeling += scores[term]
                
        if answer in negatives:
            score_feeling = 0

        if score_feeling > 0:
            general_score += 1
        elif score_feeling < 0:
            general_score -= 1

    question[individual].append(general_score)
    print general_score
    





