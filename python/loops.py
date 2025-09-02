#While loop in python
#syantax -->
# while condition
count = 1 #initail varible 
while count <= 5: #conditions
	print("Hello World!") #perfom
	count += 1 #updating condition
#
#break keyword
#If went went to stop loop you can use break keyword
#
#exmple
	
i = 1
while i < 10:
	print(i)
	if i == 5:
		break
	i += 1
#
#
#For loop 
#santax 
# for el in list:
print("For Loops")
nums = ["Fahim vai","Zahid vai","Zehad","Rakib","Sanjidha","Lamiya"]
	
for val in nums:
	print(val)
#
#
#range() function 
#santax
# range(start?,stop,step?) 
for i in range(10):
	#start and step is optional 
	print(i)
for i in range(2,20):
	print(i)

for i in range(1,20,2):
	print(i) #print all even numbars
#
#
#pass using skip loop
for i in range(10):
	pass
print("using pass")