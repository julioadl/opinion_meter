import sys

dictionary1 = open(sys.argv[1])
dictionary2 = open(sys.argv[2])

data1 = []
data2 = []
new_dict = {}

for row in dictionary1:
    data1.append(row)

for row in dictionary2:
    data2.append(row)

for item in data1:
    term, score = item.split()
    new_dict[term] = int(score)

for term in data2:
    term, score = term.split()
    if term not in new_dict: 
        new_dict[term] = -999

for term in new_dict:
    print new_dict[term], term
