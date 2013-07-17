import MapReduce_class as MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(line):
	
	answer = line.split()
	
	for words in answer:
		mr.emit_intermediate(words, 1)

def reducer(key, list_of_values):
	
	total = 0

	for v in list_of_values:
		total += v

	mr.emit(key,total)	

data = open(sys.argv[1])

mr.execute(data, mapper, reducer)
