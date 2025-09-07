#Objects and class
#create a class
class student:
	name = "Zehad"
#create Obje using class
s1 = student()
print(s1.name)
#
#using __init__() function 
class friends:
	def __init__(self,full_name,gpa):
		self.gpa = gpa
		self.name = full_name
#creating obj
f1 = friends("Khalid",4.63)
f2 = friends("Zehad",4.88)
f3 = friends("Obydul",4.63)
f4 = friends("Mahin",5.0)
print(f1.name,f1.gpa)
print(f2.name,f2.gpa)
print(f3.name,f3.gpa)
print(f4.name,f4.gpa)
#
#Methods
class welcome:
	def wel_msg(self):
		print("Welcome")
msg = welcome()
msg.wel_msg()
#
#Static method are you when not use self 
class test_static:
	@staticmethod
	def collage():
		print("Appna collage")
test1 = test_static()
test1.collage()
#
#Absutration is hide unnaccry code and show naccry code
class car():
	def __init__(self):
		self.acc = False
		self.brk = False
		self.clatuch = False
	def start(self):
		self.clatuch = True
		self.acc = True 
		print("Car is started...")
#======Abstraction====
car1 = car()
car1.start()
#======================
