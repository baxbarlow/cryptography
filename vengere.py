# Vigenere Cipher
# Arguments: string, string
# Returns: string
alphabet = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25 
}
def encrypt_vigenere(plaintext, keyword):

	key = keyword
	if len(keyword) > len(plaintext):
		key = keyword[:len(plaintext)]
	if len(keyword) < len(plaintext):
		while len(key) < len(plaintext):
			key += key
		key = key[:len(plaintext)]
	encrypted = ""
	for i in range(len(plaintext)):
		sum = alphabet.get(key[i]) + alphabet.get(plaintext[i])
		if sum > 25:
			sum -= 26
		encrypted += list(alphabet.keys())[list(alphabet.values()).index(sum)]
	return encrypted

		


# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    text = ciphertext
    key = keyword
    if len(keyword) > len(text):
	    key = keyword[:len(text)]
    if len(keyword) < len(text):
	    while len(key) < len(text):
		    key += key
	    key = key[:len(text)]
    decrypted = ""
    for i in range(len(text)):
	    sum =  alphabet.get(text[i]) - alphabet.get(key[i])
	    if sum < 0:
		    sum += 26
	    decrypted += list(alphabet.keys())[list(alphabet.values()).index(sum)]
    return decrypted




word = "ICANTWAITTOMEETYOU"
key = "OKIGETIT"
encrypted = encrypt_vigenere(word, key)
print(encrypted)
decrypted = decrypt_vigenere(encrypted, key)
print(decrypted)