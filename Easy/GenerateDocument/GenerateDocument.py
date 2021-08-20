# O(N + M + K) time | O(C + D) space
def generateDocument(characters, document):
	nonDuplicatesChars = set(characters)
	
	charsFrequency = {}
	for idx, char in enumerate(characters):
		if char not in charsFrequency:
			charsFrequency[char] = 1
		else:
			charsFrequency[char] += 1
	
	docFrequency = {}
	for idx, doc in enumerate(document):
		if doc not in docFrequency:
			docFrequency[doc] = 1
		else:
			docFrequency[doc] += 1
	
	for char in document:
		if char not in characters or charsFrequency[char] < docFrequency[char]:
			return False
	
	return True
	
# O(N + M) time | O(C) space - where C is the number of of unique characters in the characters string - Optimal solution
def generateDocument2(characters, document):
	charsFrequency = {}
	for idx, char in enumerate(characters):
		if char not in charsFrequency:
			charsFrequency[char] = 0
		
		charsFrequency[char] += 1
	
	for char in document:
		if char not in charsFrequency or charsFrequency[char] == 0:
			return False
		
		charsFrequency[char] -= 1
	
	return True