# Vigenere Cipher
# Arguments: string, string
# Returns: string
asciiVals = {
    "A": 65,
    "B": 66,
    "C": 67,
    "D": 68,
    "E": 69,
    "F": 70,
    "G": 71,
    "H": 72,
    "I": 73,
    "J": 74,
    "K": 75,
    "L": 76,
    "M": 77,
    "N": 78,
    "O": 79,
    "P": 80,
    "Q": 81,
    "R": 82,
    "S": 83,
    "T": 84,
    "U": 85,
    "V": 86,
    "W": 87,
    "X": 88,
    "Y": 89,
    "Z": 90 
}

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
#caesar decrypt


#args: string, int
#returns: string
def decrypt_caesar(ciphertext, offset):
    ciphertext.split()
    plaintext = ""
    for letter in ciphertext:
        plaintext += (list(alphabet.keys())[list(alphabet.values()).index(int(alphabet.get(letter)) - 3)])

    return plaintext
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted_word = ""
    listed = list(plaintext)
    alphabet = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, 
        "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26      
    }
    for letter in listed:
        position = alphabet[letter.upper()]
        encrypted_word += list(alphabet.keys())[list(alphabet.values()).index(position + offset)]
    return encrypted_word

def encrypt_vigenere(plaintext, keyword):

	key = keyword
	if len(keyword) > len(plaintext):
		key = keyword[:len(plaintext)]
	if len(keyword) < len(plaintext):
		while len(key) < len(plaintext):
			key += key
		key = key[:len(plaintext)]
	print(plaintext)
	print(key)
	encrypted = ""
	for i in range(len(plaintext)):
		sum = alphabet.get(key[i]) + alphabet.get(plaintext[i])
		if sum > 25:
			sum -= 26
		encrypted += list(alphabet.keys())[list(alphabet.values()).index(sum)]
	print(encrypted)

def merkle_encrypt(plaintext, public_key):
    asciiString = ""
    for letter in plaintext:
        digitList = ['0']
        binaryStr = str(bin(asciiVals.get(letter)))[2:]
        for digit in binaryStr:
            digitList.append(digit)
        print(digitList)


# Arguments: string, string
# Returns: string
#def decrypt_vigenere(ciphertext, keyword):
    
encrypt_vigenere("HELLO", "LEMON")