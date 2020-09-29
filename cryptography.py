# Cryptography project by Eddie, Bax, and Austin

import random
import math

#Alphabet dictionary
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



# Arguments: string - text to encrypt, integer - offset
# Returns: string - encrypted text
def encrypt_caesar(plaintext, offset):
    encrypted_word = ""
    if (plaintext == None):
    	return None
    listed = list(plaintext)
    for letter in listed:
        position = alphabet[letter.upper()]
        encrypted_word += list(alphabet.keys())[list(alphabet.values()).index((position + offset) % 26)]
    return encrypted_word

# Arguments: string - text to decrypt, integer - offset
# Returns: string - decrypted text
def decrypt_caesar(ciphertext, offset):
	if (ciphertext == None):
		return None
	offset %= 26
	ciphertext.split()
	plaintext = ""
	for letter in ciphertext:
		sum = int(alphabet.get(letter)) - offset
		if sum < 0:
			sum = 26 + sum
		plaintext += (list(alphabet.keys())[list(alphabet.values()).index(sum)])
	return plaintext



# Arguments: string - text to encrypt, string - keyword used for encyrption
# Returns: string - encrypted text
def encrypt_vigenere(plaintext, keyword):
	if (plaintext == None):
		return None
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
			sum %= 26
		encrypted += list(alphabet.keys())[list(alphabet.values()).index(sum)]
	return encrypted

# Arguments: string - text to decrypt, string - keyword used for decyrption
# Returns: string - deciphered text
def decrypt_vigenere(ciphertext, keyword):
	if (ciphertext == None):
	    return None
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



# Returns: tuple - a randomly generated key
def generate_private_key(n=8):
    # Generating superincreasing sequence W
    list_w = [1]
    i = 1
    sum = list_w[0]
    while len(list_w) < 8:
        list_w.append(random.randint(sum + 1, 2 * sum))
        sum = sum + list_w[i]
        i = i + 1
    w = tuple(list_w)

    # Creating integer Q as "next number" after sum
    q = random.randint(sum + 1, 2 * sum)

    # Generating integer R where R and W are coprime
    r = 0
    while math.gcd(r, q) != 1:
        r = random.randint(2, q - 1)

    # Tuple private key with W, Q, R
    private_key = (w, q, r)
    #print(private_key)
    return private_key

# Arguments: tuple (tuple, integer, integer) - the private key
# Returns: tuple - a tuple of integers as a public key
def create_public_key(private_key):
    (w_list, q, r) = private_key
    return tuple([((r * w_list[i]) % q) for i in range(8)])


# Arguments: string - the text you want to encrypt, tuple - the key used to encrypt it
# Returns: array - an array of integers

def encrypt_mhkc(plaintext, public_key):
	encryptedList = [] 
	for letter in plaintext:
		digitList = []

		#creates a binary number from the ascii value and makes it 8 bits in an array
		binaryStr = str((bin(ord(letter)))[2:].zfill(8))
		for digit in binaryStr:
			digitList.append(digit)
		c = 0

		#Sums up the bits times the public key index and creates an array with them
		for i in range(len(digitList)):
			c += (int(digitList[i]) * public_key[i])
		encryptedList.append(c)
	return encryptedList

#Arguments: array - an array of encrypted characters as integers, tuple (tuple, integer, integer) - the private key
#Returns: string - the decrypted ciphertext

def decrypt_mhkc(ciphertext, private_key):
     (W,R,Q) = private_key
     S = 1
     while Q*S%R != 1:
          S += 1
     plaintext = ""
     for c in ciphertext:
        indices = []
        C_prime = c*S%R
        for i in range(len(W)):
            if  C_prime >= W[len(W) - i - 1]:
                C_prime -= W[len(W) - i - 1]
                indices.append(1)
            else:
            	indices.append(0)
        indices.reverse()
        binaryNum = ""
        for bit in indices:
        	binaryNum += str(bit)
        plaintext += chr(int(binaryNum, 2))     
     return plaintext


private_key = generate_private_key()
public_key = create_public_key(private_key)


print(decrypt_caesar(encrypt_caesar("XYZ", 3), 3))
print(decrypt_vigenere(encrypt_vigenere("VIGNERE", "TEST"), "TEST"))
print(decrypt_mhkc(encrypt_mhkc("MHKC", public_key), private_key))