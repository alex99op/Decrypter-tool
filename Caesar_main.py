import Encrypter, Decrypter
#import time
#import os
#clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def wiki():
	print("\nWiki:\nThis software is just for learning and nothing else. Written by AWR, free for all.")

   
def main_menu():
	""" This shows the main menu """
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
	"Starts the program the user choice"
	switch = {
			"1": lambda: Decrypter.main_menu(),
			"2": lambda: Encrypter.main_menu(),
			"3": lambda: wiki(),
			"q": lambda: quit(),
			}

	return switch[user_input]() if user_input in switch else print("Did not understand that")		
 
 
main_menu()


#time.sleep(1)
#clearConsole()		
#main_menu()