import time
#import Ceasar_main
buff = []
decrypted_message = []


def convert_from_char(plain_message, user_key):
	"""Converts the decrypted message into ASCII code to easy change the value"""
	for i in plain_message:
		buff.append(ord(i) - (96 - user_key))
	convert_to_char(user_key)


def convert_to_char():
	"""Converts ASCII value to letters"""
	for i in buff:
		if i != -62: #Hvis jeg plusser inn hoppet her så vil den muligens bli modulær for å få space uansett antall hopp? LØST??
			decrypted_message.append(chr(i + 96))
		else:
			decrypted_message.append(chr(32))


def convert_to_char(user_key):
	"""Converts ASCII value to letters"""
	for i in buff:
		if i == (-64+user_key): #Hvis jeg plusser inn hoppet her så vil den muligens bli modulær for å få space uansett antall hopp? LØST??
			decrypted_message.append(chr(32))
		else:
			decrypted_message.append(chr(i + 96))

def main():
	plain_message = input("Write in your message:\n")
	user_key = int(input("What number do you want to set as a key?(Write a positive or negative number)\n"))
	convert_from_char(plain_message, user_key)
	print("This is the encrypted message, dont forget your key!\n" +''.join(decrypted_message))
 
if __name__ == '__main__':
	main()


#Gjør om alle bokstaver til tall, legg på antall hopp til tallet, converter tilbake til bokstav. DONE!
#Sette opp som funksjoner for å gjøre ting mer modulært. Sette opp Velkomstmeny? og som en funksjon så man kan komme tilbake til den.
#Flytte funksjoner til egen fil for penere kode.
#Få main funksjonen til en funksjon og 
#Bryt opp decryptering inn i egen fil, og encryptingen i sin egen fil for penere resultat og for lættis.
#Lag en options meny, der man kan endre lengde på bruteforce, "Debuggmode" for at clear screen ikke skal skje for å gjøre det lettere å finne feil osv.

#try 
#if user_key == Y: 
	
#else user_key == N:
#    bruteforce
