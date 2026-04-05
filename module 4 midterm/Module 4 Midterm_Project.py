# Importing the hashlib library and importing fernet from the cryptography library. 
import hashlib
from cryptography.fernet import Fernet

# Accept user input and converted it into bytes. 
user_input = input("Enter a message: ").encode()

# Hashing the user's input and displaying the hash.
original_hash = hashlib.sha256(user_input).hexdigest()
print(f"Original SHA-256 Hash: {original_hash}")

# Generating key for encryption and creating a fernet cipher object. 
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypting the user's input and displaying the encrypted data. 
encrypted_data = cipher.encrypt(user_input)
print(f"Encrypted Data: {encrypted_data}")

# Decrypting the encrypted data and displaying it. 
decrypted_data = cipher.decrypt(encrypted_data)
print(f"Decrypted Data: {decrypted_data.decode()}")

# Hash the decrypted data to verify integrity. 
decrypted_hash = hashlib.sha256(decrypted_data).hexdigest()
print(f"Decrypted SHA-256 Hash: {decrypted_hash}")

# Checking if the original hash matches the decrypted hash for integrity. 
if original_hash == decrypted_hash:
    print("Integrity Verified: Hashes match.")
else:
    print("Integrity Check Failed: Hashes do NOT match.")
