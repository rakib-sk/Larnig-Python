#Registion pgae
print("---------")
print("sign up: ")
user_name = input("\tEnter username: ")#username input
user_password = input("\tCreate a password: ")#user password input
print("\tAccount created!!!")#show account created!!
#
#
#
print("\n")#New line 
print("\n")#new line
check_username = input("\tEnter user name: ")#input agin user name to check == or =! 
check_user_password = input("\tEnter password: ")#input agin password to check == or =!
#
#
#logic part
if user_name == check_username and user_password == check_user_password:
	print("Login succesfull!!")
else:
	print("\tAccount not found")