import numpy as np
import csv as csv
import math
import sys

#open dictionary

afinfile_good = open(sys.argv[1]) #dictionary for the question with positive connotation
afinfile_bad = open(sys.argv[2])  #dictionary for the questions with negative connotation

# open and import into the CSV. It skips the first line as it's the header
csv_file_object = csv.reader(open(sys.argv[3], "rb"))
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
    response.append(data[individual,37])    #picks up the item of the numpy array
    response.append(data[individual,38])    #the first four items correspond to the positive 
    response.append(data[individual,39])
    response.append(data[individual,40])
    response.append(data[individual,42])    #the last four correspond to the ones with negs
    response.append(data[individual,43])
    response.append(data[individual,44])
    response.append(data[individual,45])
    question[data[individual,0]] = response #adds the items of the numpy array into one individual respone

#new dictionary
positive = [] #dictionary for the positives
negative = [] #dictionary for the negatives

#prepares the dictionary for the positives
for line in afinfile_good:
    positive.append(line)

#scores
scores_pos = {}
for item in positive:
    term, score = item.split()
    #term = term.decode('utf-8')
    scores_pos[term] = int(score)

#prepares the dictionary for the negative
for line in afinfile_bad:
    negative.append(line)

#scores
scores_neg = {}
for item in negative:
    term, score = item.split()
    #term = term.decode('utf-8')
    scores_neg[term] = int(score)

negatives = ['no', 'No', 'NO', 'none', 'NONE', 'None', 'not good', 'nothing good']

#compare with dictionary
for individual in question:
    general_score = 0
    dictionary = 0

    for answer in question[individual]:
        
        score_feeling = 0
        words = answer.split()
        
        if dictionary < 3:
            for term in scores_pos:
                for item in words: 
                    if term == item:
                        score_feeling += scores_pos[term]
                
            if answer in negatives:
                score_feeling = 0

            if score_feeling > 0:
                general_score += 1
            elif score_feeling < 0:
                general_score -= 1

            dictionary += 1

        elif dictionary > 3:
            for term in scores_neg:
                for item in words: 
                    if term == item:
                        score_feeling += scores_neg[term]
                
            if answer in negatives:
                score_feeling = 0

            if score_feeling > 0:
                general_score += 1
            elif score_feeling < 0:
                general_score -= 1

    question[individual].append(general_score)
    print general_score
    





