# Simple Login/Authentication System

# --- Sign Up ---
print("Sign Up:")
reg_username = input("Enter username: ")
reg_password = input("Enter password: ")

# --- Log In ---
print("\nLog In:")
login_username = input("Enter username: ")
login_password = input("Enter password: ")

# --- Authentication Check ---
if login_username == reg_username and login_password == reg_password:
    print(f"\nYou are successfully logged into your account. Welcome @{login_username} !")
else:
    print("\nLog In failed due to invalid password or username entered.")