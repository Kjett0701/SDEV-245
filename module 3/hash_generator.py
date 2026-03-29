# Importing the hashlib library. 
import hashlib 

# Asking the user if they would like to hash a string or file. 
user_input = input("What would you like to hash? (Type either 'string' or 'file'): ")

# If the user selects "string" as what they want to hash, then the program will ask for the string and then hash it for security. 
if user_input == "string":
    string_hash = input("Okay, type the string you would like to hash: ") 
    string_hash = hashlib.sha256(string_hash.encode()).hexdigest() 
    print("SHA-256 hash: ", string_hash)
# If the user selects "file" as what they want to hash, then the program will ask for the file location, read the file in bytes, and then hash it for security. 
elif user_input == "file":
    filename = input("Okay, type the file location: ")   
    # This try statement checks to see if the file location can be read. If it cannot, the program will give the user a "FileNotFoundError" message. 
    try:
        with open(filename, "rb") as f:
            file_bytes = f.read() 
            file_hash = hashlib.sha256(file_bytes).hexdigest() 
            print("SHA-256 hash: ", file_hash)
    except FileNotFoundError: 
        print("File not found.") 
# If the user does not type "string" or "file" the program will catch it and say that the input is invalid and will stop the program.     
else:
    print("Invalid input. Try again.") 

    