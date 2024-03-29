decrypted_message = []
bit_map = []
ALPHABET = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Æ', 'Ø', 'Å'}
brute = 13
'''
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
'''

def simple_mode():
	print("\nSimple mode:")	
	encrypted_message = input("Write inn the encrypted message:\n>")
	user_choise = input("Do you know how many jumps the ciper has?(Y/N)\n> ")
	#bit_map_appender(encrypted_message)

	if  user_choise.lower()=="y":
		user_jump = int(input("How many jumps?(Write a number)\n> "))
		decrypt(encrypted_message, user_jump)

	elif user_choise.lower() == "n": #Bruteforce up to 12 jumps
		brute = 13
		print("We will try up to 13 jumps:\n")
		for user_jump in range(1, brute):
			decrypt(encrypted_message, user_jump)
	else:
		print("I did not understand that\n>")
		main_menu()

def test():
	brute = int(input("How many jumps you want?\n> "))
	return brute


def advanced_mode_options():
	print("1. Change brutforce number from standar 13")
	print("2. Limit ASCII range")
	print("3. Ignore spacebar")
	return None


def advanced_mode():
	print("\nAdvanced mode:")
	print("1. Run with standard values")
	print("2. Options")
	print("q. Quit")
	advanced_option = input("> ")

	options = {
		"1": lambda: None,
		"2": lambda: None, #advanced_mode_options(),
		"3": lambda: None,
		"q": quit,
	}
	options.get(advanced_option, quit)()

	brute = test()#DENNE BURDE VÆRE INNI options PÅ EN ELLER ANNEN MÅTE
	encrypted_message = input("Write inn the encrypted message:\n> ")
	user_choise = input("Do you know how many jumps the ciper has?(Y/N)\n> ")

	if  user_choise.lower() == "y":
		user_jump = int(input("How many jumps?(Write a number)\n> "))
		decrypt(encrypted_message, user_jump)

	elif user_choise.lower() == "n": #Bruteforce up to 12 jumps
		print("We will try up to 13 jumps:\n")
		for user_jump in range(1, brute):
			decrypt(encrypted_message, user_jump)
			
	else:
		print("I did not understand that\n> ")
		advanced_mode()


def decrypt(encrypted_message: str, user_jump: int):#Denne tar ikke hensyn til mellomrom
	decrypted_message = ''.join(chr((ord(c) - user_jump) % 256) for c in encrypted_message) #c = character
	print(f"{user_jump}. {decrypted_message}")


def main_menu():
	print()
	print("1. Simple mode")
	print("2. Advanced mode")
	print("q. Quit")	
	user_input = input("> ")
	
	switch = {
				"1": lambda: simple_mode(),
				"2": lambda: advanced_mode(),
				"q": lambda: quit(),
				}
	return switch[user_input]() if user_input in switch else print("Did not understand that")


if __name__ == '__main__': # Legg inn når koden over er fikset til slik den trenger.
	main_menu()