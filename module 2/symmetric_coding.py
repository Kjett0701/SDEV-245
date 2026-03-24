# Get fernet from cryptography and import it so that it can be used. 
from cryptography.fernet import Fernet 

# Generate a random key for both encryption and decryption. 
key = Fernet.generate_key() 


# Uses key to encrypt and decrypt messages. 
cipher = Fernet(key) 

# This is the message we want to encrypt. 
# In order for this to be encrypted, the message must be converted into bytes. 
# The Cipher can now encrypt this message now that it's converted into bytes. 
message = "This is symmetric coding!" 
message_bytes = message.encode()

# The cipher has now encrypted the message that was converted into bytes. 
encrypted = cipher.encrypt(message_bytes) 

# This code is decrypting the encrypted message. 
decrypted = cipher.decrypt(encrypted)

# Decoding the decrypted message from bytes to human language. 
new_message = decrypted.decode() 

# Displaying the encrypted message (for fun) and showing the decoded message. 
print(encrypted)
print(new_message)