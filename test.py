import time
user_jump = 0


ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def decrypting(encrypted_message, user_jump):
    buff=[]
    decrypted_message = []
    encrypted_message = encrypted_message.upper()

    for i in encrypted_message: #gjør om hver bokstav om til tall som lagres i buff
        for x, y in enumerate(ALPHABET):
            if i == y:
                v = x + user_jump
                buff.append(v)

    
    for i in buff: #Gjør om fra tall til bokstaver og printer ut resultatet
        for z, c in enumerate(ALPHABET):
            if z == i:
                decrypted_message.append(c)
    print(f"{user_jump}." + ''.join(decrypted_message)) 







def decrypt_menu():
    encrypted_message = input("Write inn the encrypted message:\n")
    user_choise = "n"

    if user_choise == "n" or user_choise == "N": #Bruteforce up to 12 jumps
        user_jump = 1
        print("We will try up to 13 jumps:\n")
        time.sleep(1)
	
        while user_jump < 13:
            decrypting(encrypted_message, user_jump)
            user_jump += 1

    else:
        user_choise = input("I did not understand that, Do you know how many jumps?(Y/N)\n")
        decrypt_menu()


decrypt_menu()