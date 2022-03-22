import time
from tkinter import W

buff = []
decrypted_message = []


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


encrypted_message = input("Write inn the encrypted message:\n")
user_yey = input("Do you know how many jumps?(Y/N)\n")


if user_yey == "y" or user_yey == "Y":
	user_jump = int(input("How many jumps?(Write a number)\n"))
	convert_from_char(user_jump)
	print(''.join(decrypted_message))      

elif user_yey == "n" or user_yey == "N": #Bruteforce up to 10 jumps
	user_jump = 1
	print("We will try up to 10 jumps:")
	time.sleep(1)
 
	while user_jump < 11:
		convert_from_char(user_jump)
		print(f"{user_jump}." + ''.join(decrypted_message))
		user_jump += 1
		decrypted_message = []
		buff = []
else:
	user_yey = input("I did not understand that, Do you know how many jumps?(Y/N)\n")

#if __name__ == '__main__': # Legg inn når koden over er fikset til slik den trenger.
	#main()

#Gjør om alle bokstaver til tall, legg på antall hopp til tallet, converter tilbake til bokstav. DONE!
#Sette opp som funksjoner for å gjøre ting mer modulært. Sette opp Velkomstmeny? og som en funksjon så man kan komme tilbake til den.
#Flytte funksjoner til egen fil for penere kode.
#Få main funksjonen til en funksjon og 
#Bryt opp decryptering inn i egen fil, og encryptingen i sin egen fil for penere resultat og for lættis.
#Lag en options meny, der man kan endre lengde på bruteforce, "Debuggmode" for at clear screen ikke skal skje for å gjøre det lettere å finne feil osv.

#try 
#if user_yey == Y: 
	
#else:
#	user_yey == N:
#		bruteforce