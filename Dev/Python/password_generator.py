print(f"Welcome to the Password Generator!")
#num_letters = input("How many letters would you like in your password? ")

import string
string.ascii_letters
alphabet = (string.ascii_letters)#string of alphabet
#print(alphabet_list)

alphabet_list = alphabet.split()
print(alphabet_list)

count = 0
for n_letters in alphabet_list:
	count += 1

#for i in range(count):
	#alphabet_list[i] = int(alphabet_list[i])
