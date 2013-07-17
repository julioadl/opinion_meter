import random
import sys

data = open(sys.argv[1])

results = []

for line in data:
	results.append(line)

sample = []

for i in range(100):
	sample.append(random.choice(results))

for i in range(100):
	print sample[i]	
