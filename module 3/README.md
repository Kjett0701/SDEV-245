Hash.py 

hash.py is a small program that asks the user whether they want to hash a string or a file. After the user chooses, the program either takes the typed‑in string or reads the file in bytes, and then generates a hash from it. It’s a simple way to show how hashing works and how data can be turned into a secure, fixed‑length value. 

cipher_encrypt_decrypt.py 

cipher_encrypt_decrypt.py is a program that asks the user if they want to encrypt or decrypt a message. After the user chooses to encrypt or decrypt, the user is then asked to type the said message for encryption or decryption. Then they are asked how many shifts they want to apply to the message. The program then checks the message for characters, upper and lowercase characters, and special characters to then apply the shift the user requested with the ASCII range. If the character is a special character, it will be left unchanged. After everything is done, the program will show the users encrypted/decrypted message. 


digital_signature.py 

digital_signature.py is a program that creates a private key, a public key, and a message. The program then uses the private key to create a signature. After the signature is created, the program uses the public key to verify it inside of a try-except block. If the signature matches the message, and was created with the correct private key, the verification is successful. If the verification is not successful it will print an error message. 
