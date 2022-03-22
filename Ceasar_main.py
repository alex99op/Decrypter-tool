import time
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def decrypt_menu():
	print("Simple decrypt will just decrypt with letters, advanced will decypt with letters but also with the use of spesial charackters\n1.Simple\n2.Advanced\n'q' to quit\n")
	#Legg inn try else for en fin loop.	
	user_input = input()
	
 
def main_menu():
	""" This is the Main manu where it all starts """
	print("#######################")
	print("# Welcome to OFFCRYPT #")
	print("#######################")
	print('Press "q" to quit\n')
	print("1. Decrypt")
	print("2. Encrypt")
	print("3. Help")
 
	user_input = input("> ")

	if user_input == "1":
		#Go to Decrypt file/funksjonen
		print("")
  
	elif user_input == "2":
		#Go to Encrypt file/funksjon
		import Caesar_encrypter #THis is shitty code, will fix in update.
		
	elif user_input == "q" or user_input == "Q":
		quit()
  
	elif user_input == "3":
		print("Wiki\n This software is just for learning and nothing else. Written by AWR, free for all open source software.")
  
	else:
		print("Did not understand that, going back to main menu")
		time.sleep(1)
		clearConsole()
		main_menu()
 
 
main_menu()