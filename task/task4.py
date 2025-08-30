password = input("Enter a password : ")
password_length = len(password)
if password_length > 6:
  print("Done!!!")
else:
  print(password,"password is too short!!!")