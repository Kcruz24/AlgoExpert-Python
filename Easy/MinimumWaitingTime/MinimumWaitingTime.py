# O(Nlog(N^2)) time | O(1) space - at 13 min
def minimum_waiting_time(queries):
	queries.sort()
	time = 0
	
	for i in range(len(queries)):
		for j in range(i):
			time += queries[j]
			
	return time
	

# O(Nlog(N)) time | O(1) space
def minimum_waiting_time2(queries):
	queries.sort()
	time = 0
	
	for i in range(len(queries)):
		queries_left = len(queries) - (i + 1)
		time += queries[i] * queries_left
	
	return time