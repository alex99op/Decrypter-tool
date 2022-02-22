alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
decrypted_message = []

encrypted_message = input("Write inn the encrypted message\n")
encrypted_message = list(encrypted_message) #The string is converted to an array.

user_yey = input("Do you know how many jumps?(Y/N)\n")
if user_yey == "y" or user_yey == "Y":
    user_jump = input("How many jumps?(Write a number)\n")
    print(user_jump)
    print("end")
    

print(encrypted_message)

#try 
#if user_yey == Y: 
    
#else user_yey == N:
#    bruteforce

#for x, i in enumerate (encrypted_message):
 #   if i == encrypted_message[x]:
  #      print("Hello")