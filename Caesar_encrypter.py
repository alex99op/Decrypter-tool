buff = []
encrypted_message = []
bit_map = []
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


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
	to_char()


def to_char():
	for i in buff:
		for x, y in enumerate(ALPHABET):
			if i == x:
				encrypted_message.append(y.lower())
	bit_map_resolver(encrypted_message)


def encrypt_menu():
	plain_message = input("Write in your message:\n")
	user_key = int(input("What number do you want to set as a key?(Write a positive or negative number)\n"))
	bit_map_appender(plain_message)
	encrypter(plain_message, user_key)
	print("This is the encrypted message, dont forget your key!\n" +''.join(encrypted_message))
	

 
if __name__ == '__main__':
	encrypt_menu()