ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Æ', 'Ø', 'Å']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']
buff = []
encrypted_message = []
bit_map = []


def bit_map_appender(plain_message):
	for i in plain_message:
		if i == " ":
			bit_map.append(1)
		else:
			bit_map.append(0)


def bit_map_resolver(encrypted_message):
	for x, y in enumerate(encrypted_message):
		if bit_map[x] == 0:
			pass
		else:
			encrypted_message.insert(x," ")


def encrypter(plain_message, userkey):
	plain_message = plain_message.upper()
	
	for i in plain_message:
		for x, y in enumerate(ALPHABET):
			if i == y:
				placeholder = (x + userkey) % 26
				buff.append(placeholder)
		
		for x, y in enumerate(NUMBERS):
			if i == y:
				placeholder = int(i) + userkey
				buff.append(str(placeholder))
	to_char()


def to_char():
	for i in buff:
		for x, y in enumerate(ALPHABET):
			if i == x:
				encrypted_message.append(y.lower()) 
		
		for x, y in enumerate(NUMBERS):
			if i == y:
				encrypted_message.append(i)
	bit_map_resolver(encrypted_message)


def main_menu():
	plain_message = input("Write in your message:\n")
	user_key = int(input("What number do you want to set as a key?(Write a positive or negative number)\n"))
	bit_map_appender(plain_message)
	encrypter(plain_message, user_key)
	print("This is the encrypted message, dont forget your key!\n" +''.join(encrypted_message))

	

 
if __name__ == '__main__':
	main_menu()