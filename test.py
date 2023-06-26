decrypted_message = []
bit_map = []
ALPHABET = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Æ', 'Ø', 'Å'}


def bit_map_appender(encrypted_message):
	for i in encrypted_message:
		if i == " ":
			bit_map.append(1)
		else:
			bit_map.append(0)


def bit_map_resolver(decrypted_message):
	for x, y in enumerate(decrypted_message):
		if bit_map[x] == 1:
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
					v = v + 29
				buff.append(v)

    
	for i in buff: #Gjør om fra tall til bokstaver og printer ut resultatet
		for z, c in enumerate(ALPHABET):
			if z == i:
				decrypted_message.append(c)
	bit_map_resolver(decrypted_message)
	print(f"{user_jump}. " + ''.join(decrypted_message))


def simple_mode():
	print("\nSimple mode:")	
	startup(1)



def advanced_mode():
	print("\nAdvanced mode:")
	print("1.Run with standard values")
	print("2.Options")
	print("q.Quit")
	advanced_option = input(">")

	options = {
		'1': lambda: startup(2),
		'2': lambda: print("change bruteforce number, limit ASCII range\n"),
		'q': quit,
	}
	options.get(advanced_option, quit)()




def advanced_decrypt(encrypted_message: str, user_jump: int) -> str:
	decrypted_message = ''.join(chr((ord(c) - user_jump) % 256) for c in encrypted_message) #c = character
	print(f"{user_jump}. {decrypted_message}")




def startup(version: int, brute = 13):
	
	if version == 0: print("\nSimple mode:")
	encrypted_message = input("Write inn the encrypted message:\n>")
	user_choise = input("Do you know how many jumps the ciper has?(Y/N)\n>")
	bit_map_appender(encrypted_message)

	if  user_choise.lower()=="y":
		user_jump = int(input("How many jumps?(Write a number)\n>"))
		if version == 1:
			decrypting(encrypted_message, user_jump)
		else:
			advanced_decrypt(encrypted_message, user_jump)
	
	elif user_choise.lower() == "n": #Bruteforce up to 12 jumps
		brute = 13
		print("We will try up to 13 jumps:\n")
		for user_jump in range(1, brute):
			if version == 1:
				decrypting(encrypted_message, user_jump)
			else:
				advanced_decrypt(encrypted_message, user_jump)
	else:
		print("I did not understand that\n>")
		main_menu()



def main_menu():
	print("1.Simple mode")
	print("2.Advanced mode")
	print("q.Quit")	
	user_input = input(">")
	
	switch = {
				"1": lambda: simple_mode(),
				"2": lambda: advanced_mode(),
				"q": lambda: quit(),
				}
	return switch[user_input]() if user_input in switch else print("Did not understand that")


if __name__ == '__main__': # Legg inn når koden over er fikset til slik den trenger.
	main_menu()


