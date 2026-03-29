# Importing modules from the cryptography library. 
from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.hazmat.primitives import hashes 
 

# Creating the private key. 
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size= 2048
) 

# Creating the public key. 
public_key = private_key.public_key() 

# This is the message that needs to be signed. 
message = b"This is a random message for this assignment!" 

# Signing the message with the private key. 
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256(),
) 

# Trying to verify the signature. 
try: 
    public_key.verify(
        signature, 
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    ) 
    # If the signature is valid, it will print this message. 
    print("Signature is valid!") 
# If the signature is invalid, it will print this message. 
except Exception as e: 
    print("Invalid signature!")


