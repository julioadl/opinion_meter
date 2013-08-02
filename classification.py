import sys

dictionary = open(sys.argv[1])
data = []

for row in dictionary:
    data.append(row)

new_dict = []

for row in data:
    score = int(row.split()[-1])
    if score != 0:
        word = row.split()[:-1]
        new_dict.append(word[0])

for item in new_dict:
    print item
