#Using del keyword to used to delet any class and objects 
#del s1,s1.name
class animal:
	def __init__(self,name):
		self.name = name
a1 = animal("Dog")
print(a1.name)
#if i delet this obj i can use del keyword 
del a1.name
#
#Private attribute and method 
#If i went any class privet i can use __ 
class account:
	def __init__(self,acc_name,acc_pass):
		self.acc_name = acc_name
		self.__acc_pass = acc_pass #acc_pass are privete
a1 = account("name","Qaw")
print(a1.acc_name)
#print(a1.acc_pass) give me erorr beacuse a1.acc_pass are private
#
#
#Inheritance are used to prent obj use to child obj
#class car:
#.......
#class Tyotacar(car):
#.......
class car:
	@staticmethod
	def start():
		print("Car started!....")
	@staticmethod
	def stop():
		print("Car stoped....")
class TyotaCar(car):
	#use inheritance 
	def __init__(self,brand):
		self.brand = brand
car1 = TyotaCar("Fortuner")
car2 = TyotaCar("Lexus")
print(car1.brand)
print(car2.brand)
car1.start()#Normally this is give me erorr.. But i is noy give me erorr.beacuse i am use inheritance 
car1.start()
#
#Multi-level inheritance 
class Fortuner(TyotaCar):
	def __init__(self,type):
		self.type = type
carType1 = Fortuner("Desel")
carType1.start()
#
#Multi inheritance 
#If i use multiple class in one Class that is a multiple inheritance
#classC(A,B,C..........n)
#exmple
class A:
	varA = "Welcome to class A"
class B:
	varB = "Welcome to class B"
class C(A,B):
	varC = "Welcome to class C"
c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
#
#
#super method ব্যবহার করা হয় class এর একটা constructor এর কোড অন্য constructor এ ব্যবহার এর জন্য ব্যবহার করা হয়
class BMW:
	def __init__(self,type):
		self.type = type
	@staticmethod
	def start():
		print("Car started!.....")
	@staticmethod
	def stop():
		print("Car stoped!..")
class BMWcar(BMW):
	def __init__(self,name,type):
		#How i can you type in this constuctor?
		#Now i can use super method
		super().__init__(type)
		self.name = name
		super().start()
BMWcar1 = BMWcar("Lamborghini","Electric")
print(BMWcar1.type)
#
#classmethod
#classmethod are use to change class property using objects 
class studentsName:
	name = "anonymoua"
	@classmethod
	def change_name(scl,name):
		scl.name = name
st1 = studentsName()
st1.change_name("Zehad")
print(st1.name)
print(studentsName.name)
#
#Polymorphism 
#Dender function 
class complex:
	def __init__(self,real,img):
		self.real = real
		self.img = img
	def showNumbar(self):
		print(self.real,"i +",self.img,"j")
	def __add__(self,num):
		newReal = self.real + num2.real
		newImg = self.img + num2.img
		return complex(newReal,newImg)
num1 = complex(1,3)
num1.showNumbar()
num2 = complex(2,4)
num2.showNumbar()
num3 = num1 + num2
print("---------------")
num3.showNumbar()