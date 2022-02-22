alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

encrypted_message = input("Write inn the encrypted message\n")
encrypted_message = list(encrypted_message) #The out is converted to an array.
decrypted_message = encrypted_message


user_yey = input("Do you know how many jumps?(Y/N)\n")
if user_yey == "y" or user_yey == "Y":
    user_jump = input("How many jumps?(Write a number)\n")
   
    for x, i in enumerate(encrypted_message):
       for z, e in enumerate(alfabet):
           if i == alfabet[z]:
             decrypted_message[x].append(alfabet[e+user_jump]) 

    

print(encrypted_message)
print(decrypted_message)


#gjør om alle bokstaver til tall, legg på antall hopp til tallet, converter tilbake til bokstav.

#try 
#if user_yey == Y: 
    
#else user_yey == N:
#    bruteforce

#for x, i in enumerate (encrypted_message):
 #   if i == encrypted_message[x]:
  #      print("Hello")