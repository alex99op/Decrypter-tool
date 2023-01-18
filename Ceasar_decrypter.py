decrypted_message = []
bit_map = []
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Æ', 'Ø', 'Å']

def bit_map_appender(encrypted_message):
	for i in encrypted_message:
		if i == " ":
			bit_map.append(1)
		else:
			bit_map.append(0)


def bit_map_resolver(decrypted_message):
	for x, y in enumerate(decrypted_message):
		if bit_map[x] == 0:
			pass
		else:
			decrypted_message.insert(x," ")


def decrypting(encrypted_message, user_jump):
	buff=[]
	decrypted_message = []
	encrypted_message = encrypted_message.upper()

	for i in encrypted_message: #gjør om hver bokstav om til tall som lagres i buff
		for x, y in enumerate(ALPHABET):
			if i == y:
				v = x - user_jump
				if v < 0:
					v = v + 26
				buff.append(v)

    
	for i in buff: #Gjør om fra tall til bokstaver og printer ut resultatet
		for z, c in enumerate(ALPHABET):
			if z == i:
				decrypted_message.append(c)
	bit_map_resolver(decrypted_message)
	print(f"Trying with {user_jump} rotation: " + ''.join(decrypted_message))



'''
#This is for the advanced version with the hole askii 
def convert_from_char(user_jump):
	"""Converts the decrypted message into ASCII code to easy change the value"""
	for i in encrypted_message:
		buff.append(ord(i) - (96 - user_jump))
	convert_to_char(user_jump)


def convert_to_char():
	"""Converts ASCII value to letters"""
	for i in buff:
		if i != -62: #Hvis jeg plusser inn hoppet her så vil den muligens bli modulær for å få space uansett antall hopp? LØST??
			decrypted_message.append(chr(i + 96))
		else:
			decrypted_message.append(chr(32))


def convert_to_char(user_jump):
	"""Converts ASCII value to letters"""
	for i in buff:
		if i == (-64+user_jump): #Hvis jeg plusser inn hoppet her så vil den muligens bli modulær for å få space uansett antall hopp? LØST??
			decrypted_message.append(chr(32))
		else:
			decrypted_message.append(chr(i + 96))
'''

def decrypt_menu():
	encrypted_message = input("Write inn the encrypted message:\n")
	user_choise = input("Do you know how many jumps the ciper has?(Y/N)\n")
	bit_map_appender(encrypted_message)


	if  user_choise == "Y" or user_choise =="y":
		user_jump = int(input("How many jumps?(Write a number)\n"))
		decrypting(encrypted_message, user_jump)   


	elif user_choise == "n" or user_choise == "N": #Bruteforce up to 12 jumps
		user_jump = 1
		print("We will try up to 13 jumps:\n")
	
		while user_jump < 13:
			decrypting(encrypted_message, user_jump)
			user_jump += 1

	else:
		user_choise = input("I did not understand that, Do you know how many jumps?(Y/N)\n")
		decrypt_menu()





if __name__ == '__main__': # Legg inn når koden over er fikset til slik den trenger.
	decrypt_menu()