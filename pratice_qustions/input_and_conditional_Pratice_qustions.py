fast_numbar = int(input("Enter fast numbar: "))
secound_numbar = int(input("Enter scound numbar: "))
third_numbar = int(input("Enter third numbar: "))
if fast_numbar > secound_numbar and fast_numbar > third_numbar:
  print(fast_numbar,"This is large numbar")
elif secound_numbar > fast_numbar and secound_numbar > third_numbar:
  print(secound_numbar,"This is a large numbar")
else:
  print(third_numbar,"This is a large numbar.")