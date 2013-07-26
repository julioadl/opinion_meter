import numpy as np
import csv as csv
import math
import sys
import MapReduce_class as MapReduce

#Mapper and Reducer from MapReduce.py

def mapper(line):

        answer = line.split()

        for words in answer:
                mr.emit_intermediate(words, 1)

def reducer(key, list_of_values):

        total = 0

        for v in list_of_values:
                total += v

        mr.emit(key,total)

#open and import into the CSV. Skips the header
csv_file_object = csv.reader(open(sys.argv[1], "rb"))
header = csv_file_object.next()
data = []

#fill in the data into a list:
for row in csv_file_object:
    data.append(row)

#new list that contains the strings
answers = []
for item in range(len(data)):
    answers.append(data[item][19])

#prints answers
#list of words to ommit
#instead of printing the results, it appends it to list data2 to be read by MapReduce.py
data1 = []
not_print = ['__NA__', 'DK', 'dk', 'Dk', 'dono']
for item in answers:
    if item not in not_print:
        data1.append(item)

#calls MapReduce_class
mr = MapReduce.MapReduce()
data2 = []
mr.execute(data1, mapper, reducer, data2)

#now calls new_dict.py

dictionary1 = open(sys.argv[2])

data_dictionary = []
new_dict = {}

for row in dictionary1:
    data_dictionary.append(row)

for item in data_dictionary:
    term, score = item.split()
    new_dict[term] = int(score)

for term in data2:
    if term not in new_dict:
        new_dict[term] = -999

for term in new_dict:
    print new_dict[term], term
