

# This block of code asks the user if they wish to encrypt or decrypt their message.
# This also tells the user to type their message and how many shifts they want to apply.   
choice = input("Do you want to encrypt or decrypt your message?: ").lower()   
message = input("Okay, type your message: ") 
shift = int(input("How many shifts would you like for your message: ")) 

# If the user chooses the "encrypt" option, the program starts with a blank encrypted message to build off of. 
if choice == "encrypt":
    encrypted_message = ""
    # For the characters (letters) in the message, the program will check if the characters are in the alphabet.
    for char in message: 
        if char.isalpha():
             # If the characters (letters) are uppercase, reverse the shift using the ASCII range for uppercase letters. 
            if char.isupper():
                encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65) 
                # If the characters (letters) are not uppercase,  reverse the shift using the ASCII range for lowercase letters.
            else:
                encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
        # If the character is not in the alphabet, it will just add it to the message unchanged. 
        else:
            encrypted_message += char 
    print("Encrypted message:", encrypted_message) 

# If the user chose the "decrypt" option, the program will start with a blank decrypted message to build off of. 
elif choice == "decrypt":
    decrypted_message = "" 
    # For the characters (letters) in the message, the program will check if the characters are in the alphabet.
    for char in message: 
        if char.isalpha():
             # If the characters (letters) are uppercase, apply the shift using the ASCII range for uppercase letters. 
            if char.isupper(): 
                decrypted_message += chr((ord(char) - 65 - shift) % 26 + 65) 
            # If the characters (letters) are not uppercase, apply the shift using the ASCII range for lowercase letters.
            else:
                decrypted_message += chr((ord(char) - 97 - shift) % 26 + 97)
        # If the character is not in the alphabet, it will just add it to the message unchanged. 
        else:
            decrypted_message += char 
    print("Decrypted message:", decrypted_message)  
# If a user types something other than encrypt or decrypt, the program will give them an invalid message. 
else:
    print("Invalid input. Select encrypt or decrypt.")
