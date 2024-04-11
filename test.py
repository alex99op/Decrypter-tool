ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Æ', 'Ø', 'Å']
TALL = ['0','1','2','3','4','5','6','7','8','9']

buff = []
encrypted_message = []

plain_message = "abc12"
userkey = 8



def encrypter(plain_message, userkey):
	plain_message = plain_message.upper()
	
	for i in plain_message:
		for x, y in enumerate(ALPHABET):
			if i == y:
				placeholder = (x + userkey) % 26
				buff.append(placeholder)
    
		for x, y in enumerate(TALL):
			if i == y:
				placeholder = int(i) + userkey
				if placeholder > 9:
					placeholder = placeholder - 10 
				buff.append(str(placeholder))
	to_char()
 
 
def to_char():
	for i in buff:
		for x, y in enumerate(ALPHABET):
			if i == x:
				encrypted_message.append(y.lower()) 
		
  
		for x, y in enumerate(TALL): #BUGG: Hvis tallet blir for stort (utenfor tall range) fjernes tallet, på linje 24 har jeg gjort om 10 til 0.
										#   Spørsmålet er om tallet skal bli gjort om til et lavere tall, eller bli gjort om til bokstav.
										#   Samme gjelder for bokstaver som går utenfor range, skal dette bli gjort om til tall?
										#	Hvem er først tall så bokstaver som i HEX eller bokstaver så tall??????
			if i == y:
				encrypted_message.append(i)
	print(encrypted_message)
 
 
encrypter(plain_message, userkey)
