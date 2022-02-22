buff = []
decrypted_message = []


def bytterf(user_jump):
	for i in encrypted_message:
		buff.append(ord(i) -(96-user_jump))
	byttert()


def byttert():
	for x, i in enumerate(buff):
		decrypted_message.append(chr(i + 96))


encrypted_message = input("Write inn the encrypted message\n")
user_yey = input("Do you know how many jumps?(Y/N)\n")


if user_yey == "y" or user_yey == "Y":
	user_jump = int(input("How many jumps?(Write a number)\n"))
	bytterf(user_jump)


for x, i in enumerate(decrypted_message):
	if i == '!':
		decrypted_message[x] = chr(32)

        
print(''.join(decrypted_message))

#gjør om alle bokstaver til tall, legg på antall hopp til tallet, converter tilbake til bokstav.
#Sette opp som funksjoner for å gjøre ting mer modulært.

#try 
#if user_yey == Y: 
	
#else user_yey == N:
#    bruteforce