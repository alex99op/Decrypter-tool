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

def terminal_input():
	pass

#simple_decrypt må bli skrevet om til å ikke akseptere ascii. Bruke kanskje encrypter metoden?
def simple_decrypt(encrypted_message: str, user_jump: int):#Denne tar ikke hensyn til mellomrom
	decrypted_message = ''.join(chr((ord(c) - user_jump) % 256) for c in encrypted_message) #c = character
	return decrypted_message

def simple_mode():
	print("\nSimple mode:")	
	encrypted_message = input("Write inn the encrypted message:\n>")
	user_choise = input("Do you know how many jumps the ciper has?(Y/N)\n> ")
	#bit_map_appender(encrypted_message)

	if  user_choise.lower()=="y":
		user_jump = int(input("How many jumps?(Write a number)\n> "))
		decrypted_message = simple_decrypt(encrypted_message, user_jump)
		aski_fixer = []
		for i in decrypted_message:
			aski_fixer.append(i)
			if i == "\x1e":
				aski_fixer.pop()
				aski_fixer.append(" ")
		for i in aski_fixer: print(i, end= "")

  
	elif user_choise.lower() == "n": #Bruteforce up to 12 jumps
		brute = 13
		tall = 0
		print("We will try up to 13 jumps:\n")
		for user_jump in range(1, brute):
			tall += 1
			decrypted_message = simple_decrypt(encrypted_message, user_jump)
			aski_fixer = []
			for i in decrypted_message:
				aski_fixer.append(i)
				if i == "\x1e":
					aski_fixer.pop()
					aski_fixer.append(" ")
			if tall <= 9: print(f"{tall}. ", end= "")
			else: print(f"{tall}.", end= "")
			for i in aski_fixer: print(f"{i}", end= "")
			print()
   
	else:
		print("I did not understand that\n>")
		main_menu()



def advanced_mode():
	print("\nAdvanced mode:")
	print("1. Run with standard values")
	print("2. Options")
	print("q. Quit")
	advanced_option = input("> ")

	options = {
		'1': lambda: None,
		'2': lambda: print("#########\n1. Change bruteforce number\n2. Limit ASCII range\n3. Ignore spacebar#########"),#Få ut som egen funksjon
		'q': quit,
	}
	options.get(advanced_option, quit)()


	encrypted_message = input("Write inn the encrypted message:\n")
	user_choise = input("Do you know how many jumps the ciper has?(Y/N)\n")

	if  user_choise.lower() == "y":
		user_jump = int(input("How many jumps?(Write a number)\n> "))
		advanced_decrypt(encrypted_message, user_jump)

	elif user_choise.lower() == "n": #Bruteforce up to 12 jumps
		brute = 13
		print("We will try up to 13 jumps:\n")
		for user_jump in range(1, brute):
			advanced_decrypt(encrypted_message, user_jump)
			
	else:
		print("I did not understand that\n> ")
		advanced_mode()


def advanced_decrypt(encrypted_message: str, user_jump: int):#Denne tar ikke hensyn til mellomrom  #Kan jo kanskje putte inn bitmap før og etter første linje her?? 
	decrypted_message = ''.join(chr((ord(c) - user_jump) % 256) for c in encrypted_message) #c = character
	print(f"{user_jump}. {decrypted_message}")


def main_menu():
	print()
	print("1. Simple mode")
	print("2. Decrypt from ssh")
	print("3. Advanced mode")
	print("q. Quit")	
	user_input = input("> ")
	
	switch = {
				"1": lambda: simple_mode(),
				"2": lambda: terminal_input(),
				"3": lambda: advanced_mode(),
				"q": lambda: quit(),
				}
	return switch[user_input]() if user_input in switch else print("Did not understand that")


if __name__ == '__main__': # Legg inn når koden over er fikset til slik den trenger.
	main_menu()
