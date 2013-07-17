import numpy as np
import csv as csv
import math
import sys

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
    answers.append(data[item][8])

#prints answers
#list of words to ommit
not_print = ['__NA__', 'DK', 'dk', 'Dk', 'dono']
for item in answers:
    if item not in not_print:
        print item
