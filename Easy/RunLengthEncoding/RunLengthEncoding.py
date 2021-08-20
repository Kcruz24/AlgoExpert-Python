# O(N) time | O(N) space
def runLengthEncoding(string):
	encoded = ""
	counter = 0
	
	for idx in range(len(string) - 1):
		counter += 1
		
		if counter == 9 or string[idx] != string[idx + 1]:
			encoded += f"{counter}{string[idx]}"
			counter = 0
	
	counter += 1
	encoded += f"{counter}{string[len(string) - 1]}"
		
	return encoded