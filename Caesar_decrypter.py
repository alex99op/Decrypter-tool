buff = []
decrypted_message = []


def bytterf(user_jump):
	for i in encrypted_message:
<<<<<<< Updated upstream
		buff.append(ord(i) -(96-user_jump))
	byttert()


def byttert():
	for x, i in enumerate(buff):
		decrypted_message.append(chr(i + 96))

=======
		buff.append(ord(i) - (96 - user_jump))
	convert_to_char(user_jump)


def convert_to_char(user_jump):
	"""Converts ASCII value to letters"""
	for i in buff:
		print(i)
		if i == (-64+user_jump): #Hvis jeg plusser inn hoppet her så vil den muligens bli modulær for å få space uansett antall hopp?
			decrypted_message.append(chr(32))
		else:
			decrypted_message.append(chr(i + 96))
   
>>>>>>> Stashed changes

encrypted_message = input("Write inn the encrypted message\n")
user_yey = input("Do you know how many jumps?(Y/N)\n")


if user_yey == "y" or user_yey == "Y":
	user_jump = int(input("How many jumps?(Write a number)\n"))
	bytterf(user_jump)

"""
for x, i in enumerate(decrypted_message):
<<<<<<< Updated upstream
	if i == '!':
		decrypted_message[x] = chr(32)

=======
		if i == '!':
			decrypted_message[x] = chr(32)
"""
>>>>>>> Stashed changes
        
print(''.join(decrypted_message))

#gjør om alle bokstaver til tall, legg på antall hopp til tallet, converter tilbake til bokstav.
#Sette opp som funksjoner for å gjøre ting mer modulært.

#try 
#if user_yey == Y: 
	
#else user_yey == N:
#    bruteforce