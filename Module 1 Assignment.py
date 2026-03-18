# Hardcoded username and role. 
current_user = {
    "user" : "Greg",
    "role" : "Administrator"
} 

# Protected actions/routes. Roles created: "User" and "Administrator"
def admin_function(): 
    if current_user["role"] == "Administrator":
        print("You are the administrator.") 
    else:
        print("Access denied. You need to be an administrator.")  


def user_function():
    if current_user["role"] == "User":
        print("You are a user.") 
    else:
        print("Access denied. You are not a user.") 

# Login simulation. 
print(f"Logged in as: {current_user["user"]} ({current_user["role"]})") 

# Simulated endpoints. 
print("\nTrying admin action:") 
admin_function() 

print("\nTrying user action:") 
user_function()


# Comment on CIA Triad. 
## This script shows the Confidentiality part of the CIA triad. Only users with the correct role can access certain actions, and anyone without the right permissions gets denied. 








