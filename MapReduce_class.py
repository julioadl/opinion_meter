class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = {}

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, key, total):
	self.result.setdefault(key, [])
	self.result[key].append(total)

    def execute(self, data, mapper, reducer):
        for line in data:
            mapper(line)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        for item in self.result:
            print item, 0
