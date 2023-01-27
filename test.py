import Caesar_encrypter, Caesar_decrypter

def wiki():
	print("\nWiki:\nThis software is just for learning and nothing else. Written by AWR, free for all open source software.")


def main_menu():
    """ This is the Main menu where it all starts """
    
    print("#######################")
    print("# Welcome to OFFCRYPT #")
    print("#######################")
    print('Press "q" to quit\n')
    print("1. Decrypt")
    print("2. Encrypt")
    print("3. Help")
    
    user_input = input("> ").lower()
    sub_menu(user_input)


def sub_menu(user_input):
	"Starts the program the user chose"
	
	switch = {
			"1": lambda: Caesar_decrypter.decrypt_menu(),
			"2": lambda: Caesar_encrypter.encrypt_menu(),
			"3": lambda: wiki(),
			"q": lambda: quit(),
			}
	
	return switch[user_input]() if user_input in switch else print("Did not understand that")


main_menu()