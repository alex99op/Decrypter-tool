import time
#from tkinter import W

buff = []
decrypted_message = []
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def decrypting(encrypted_message, userjump):
	encrypted_message = encrypted_message.upper()
	
	for i in encrypted_message:
		for x, y in enumerate(ALPHABET):
			if i == y:
				buffed = x
				if (x - userjump) <= 0 or x <= 0:
					buffed = x + 26 
				placeholder = (buffed - userjump)
				buff.append(placeholder)
	to_char()


def to_char():
	for i in buff:
		for x, y in enumerate(ALPHABET):
			if i == x:
				decrypted_message.append(y.lower())


'''
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


	if  user_choise == "Y" or user_choise =="y":
		user_jump = int(input("How many jumps?(Write a number)\n"))
		decrypting(encrypted_message, user_jump)
		print("The decrypted message is:\n"+''.join(decrypted_message))     


	elif user_choise == "n" or user_choise == "N": #Bruteforce up to 12 jumps
		user_jump = 1
		print("We will try up to 13 jumps:\n")
		time.sleep(1)
	
		while user_jump < 13:
			decrypting(encrypted_message, user_jump)
			print(f"{user_jump}." + ''.join(decrypted_message))#her er det no problemer???????????
			#print(f"{user_jump} og decryptert ord")
			user_jump += 1
			decrypted_message = []
			buff = [] 
	else:
		user_choise = input("I did not understand that, Do you know how many jumps?(Y/N)\n")
		decrypt_menu()


if __name__ == '__main__': # Legg inn når koden over er fikset til slik den trenger.
	decrypt_menu()
