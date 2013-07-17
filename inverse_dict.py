import sys

dictionary = open(sys.argv[1])
data = []

for line in dictionary:
	data.append(line)

final_dict = {}

for item in data:
	score, term = item.split()
	final_dict[term] = int(score)	

for term in final_dict:
	print term, final_dict[term]
