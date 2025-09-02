#print numbars 1 to 100 using while loop
#
#
print("print numbars 1 to 100 using while loop")
numbar = 1
while numbar <= 100:
    print(numbar)
    numbar += 1
    
print("print 100 to 1 using while loop")
#print 100 to 1 using while loop
#
#
reverse_numbars = 100
while reverse_numbars <= 1:
    print(reverse_numbars)
    reverse_numbars -= 1
    
#Print the multipilications table of a numbars
#
#
print("Print the multipilications table of a numbars")
n = 3
i = 1
while i <= 10:
    print(n*i)
    i += 1
    
#Print the element of the following list using  loop
#
#
print("Print the element of the following list using  loop")
num = [2,4,8,10,40,80,20]
i = 0
while i < len(num):
    print(num[i])
    i += 1
    
#Search for a numbar x in this touple using while loop
#
#
print("Search for a numbar x in this touple using while loop")
numbars = (20,10,30,20,0,20,80)
x = 20
i = 0
while i < len(numbars):
    if numbars[i] == x:
        print("Founded!",x)
        break
    else:
    	print("founding")
    i += 1    
#
#using continue 
k = 1
while i <= 100:
	if i%2 == 0:
		i += 1
		continue 
	print(i)
	i += 1
#
#
#
#For loop
#Print the element of the following  list using for loop
print("Print the element of the following  list using for loop")
num_list = [1,2,3,4,5,6,7,8,9,0,22,33,55,66,88,99]
for val in num_list:
	print(val)
#
#
#Search for a numbar x in the touple
print("Search for a numbar x in the touple")
tup_numbar = (1,4,6,8,9,5,10,30)
x = 30
for val in tup_numbar:
	if val == x:
		print(val,"is founded!")
		break
#
#
#Print numbar 1 to 100 using for and range()
print("Print numbar 1 to 100")
for i in range(0,101):
	print(i)

#
#print numbar 100 to 1 usig for and range()
print("print numbar 100 to 1 usig for and range()")
for i in range(101,0,-1):
	print(i)
#
#
#Print the multiplication table for a numbar n
print("Print the multiplication table for a numbar n")
mul_n = int(input("Enter a numbar: "))
for i in range(1,11):
	print(n*i)
#
#
#WAP to find sum of first n numbar
print("WAP to find sum of first n numbar") 
n = 0
sum = 0
while n <= 5:
	n += 1
	sum += n
print(sum)
#
#
#Wap to find the factrioal of n numbars

