# O(N) time | O(K) space - where K is the number of letters in the given string
def caesar_cipher_encryptor(string, key):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	encrypted_msg = ''
	
	for i in range(len(string)):
		encrypted_letter = (alphabet.index(string[i]) + key) % 26
		encrypted_msg += alphabet[encrypted_letter]
	
	return encrypted_msg