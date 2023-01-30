#Bugg med space blir til konstanter, fixed, space er nr 32.


user_jump = -1
encryped_message = 'aHei og sånt abc123 .. øæå a'
decrypted_message = []


for character in encryped_message:
    print(f"{ord(character)} ", end='')
    if ord(character) == 32:
        decrypted_message.append(ord(character))
    else:
        decrypted_message.append(ord(character)+user_jump)
print(f"\n{decrypted_message}")

print(encryped_message)
for character in decrypted_message:
    print(chr(character), end="")
    
