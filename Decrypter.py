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

	for i in encrypted_message: #Gjør om hver bokstav om til tall som lagres i buff
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


def advanced_decrypt(encrypted_message, user_jump):
	for character in encrypted_message:
		if ord(character) == 32:
			decrypted_message.append(ord(character))
		else:
			decrypted_message.append(ord(character)+user_jump)

	for character in decrypted_message:
		print(chr(character), end="")


def main_menu():
	print('\nSimple mode will only change the letters, advanced mode will change every letter and spesial characters:\n1. Simple\n2. Advanced\nPress "q" to quit\n')
	advanced_choice = input("> ")
	if advanced_choice == "1":
		print("\nSimple mode:")
	elif advanced_choice == "2":
		print("\nAdvanced mode:\n1. Decrypt message\n2. Options \n> ")
	elif advanced_choice == "q" or advanced_choice == "Q":
		quit()

	encrypted_message = input("Write inn the encrypted message:\n")
	bit_map_appender(encrypted_message)
	user_choise = input("Do you know how many jumps the ciper has?(Y/N)\n")

	if  user_choise == "Y" or user_choise =="y":
		user_jump = int(input("How many jumps?(Write a number)\n"))
		if advanced_choice == "1":
			decrypting(encrypted_message, user_jump)
		else:
			advanced_decrypt(encrypted_message, user_jump)

	elif user_choise == "n" or user_choise == "N": #Bruteforce up to 12 jumps
		user_jump = 1
		brute = 13
		print("We will try up to 13 jumps:\n")
	
		while user_jump < brute:
			decrypting(encrypted_message, user_jump)
			user_jump += 1

	else:
		user_choise = input("I did not understand that, Do you know how many jumps?(Y/N)\n")
		main_menu()





if __name__ == '__main__': # Legg inn når koden over er fikset til slik den trenger.
	main_menu()