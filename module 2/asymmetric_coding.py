# Grabbing the Fernet module from the cryptography class. 
from cryptography.fernet import Fernet 

# Grabbing the RSA import from the cryptography class. 
from cryptography.hazmat.primitives.asymmetric import rsa, padding 

# Grabbing the Hashes import from the cryptography class. 
from cryptography.hazmat.primitives import hashes

# Generates a random key for encryption and decryption.
key = Fernet.generate_key() 

# Generating a private key with fast speed and a big size for secruity purposes. 
private_key = rsa.generate_private_key(
    public_exponent=65537, 
    key_size=2048
)

# Generating a public key from the private key. 
public_key = private_key.public_key()  

message = b"This is asymmetric coding!" 

# Encrypting the message. 
encrypted_message = public_key.encrypt(
    message,
    # This helps with keeping things random and secure. 
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

# The encrypted version of the message. 
print("Encrypted:", encrypted_message)

# Decrypting the message. 
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

# Displaying the decrypted message. 
print("Decrypted:", decrypted_message)
                                       
                                       

