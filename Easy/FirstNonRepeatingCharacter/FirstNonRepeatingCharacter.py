# O(N) time | O(1) space - Is constant space because our hash table will never have more than 26 english alphabet letters
def firstNonRepeatingCharacter(string):
	charTable = {}
	
	for char in string:
		if char not in charTable:
			charTable[char] = 1
		else:
			charTable[char] += 1
	
	nonRepeatingChar = 0
	nonRepeatingCharIdx = -1
	
	if len(charTable) > 0 and 1 in charTable.values():
		nonRepeatingChar = min(charTable, key=charTable.get)
		nonRepeatingCharIdx = string.index(nonRepeatingChar)
	 
	return nonRepeatingCharIdx


# O(N) time | O(1) space - Is constant space because our hash table will never have more than 26 english alphabet letters
def firstNonRepeatingCharacter2(string):
	charTable = {}
	
	for char in string:
		charTable[char] = charTable.get(char, 0) + 1
	
	for idx, char in enumerate(string):
		if charTable[char] == 1:
			return idx
	 
	return -1