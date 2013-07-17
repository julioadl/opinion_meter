import numpy as np
import csv as csv
import math

#open dictionary

afinfile = open("/Users/julioadl/Desktop/Scotto-Drones/dictionary2.txt")

# open and import into the CSV. It skips the first line as it's the header
csv_file_object = csv.reader(open("/Users/julioadl/Desktop/Scotto-Drones/drones.csv", "rb"))
header = csv_file_object.next()
data = []

#fill the data into a list
for row in csv_file_object:
    data.append(row)

#new list that contains tuples of (id, string)
#question key: question1
question1 = []
for id_answ in range(len(data)):
    question1.append((id_answ, data[id_answ][8]))

response1 = dict(ScotA_1a_1)

#new dictionary
dictionary = []
negatives = ['no', 'No', 'NO', 'none', 'NONE', 'None', 'not good', 'nothing good']
neutrals = ['Nothing', 'nothing']

for line in afinfile:
    dictionary.append(line)

#scores
scores = {}
for item in dictionary:
    term, score = item.split()
    #term = term.decode('utf-8')
    scores[term] = float(score)

#compare with dictionary
for id_answ in response1:
    score_feeling = 0
    answer = response1[id_answ]  #calls the "answer" from the question

    for term in scores:
        if term in answer:
            score_feeling = score_feeling + scores[term]
                
    if len(answer.split()) == 1:
        if answer in negatives:
            score_feeling = -1
       #elif answer in neutrals:
        #score_feeling = 0
   
   # if len(answer.split()) == 2:
	#if answer in negatives:
	   #score_feeling = -1
    
    DK = ['__NA__', 'dk', 'Dk', 'DK', 'd/k', 'dono']
	
    if response1[id_answ] not in DK:
        print response1[id_answ], score_feeling
        
    





