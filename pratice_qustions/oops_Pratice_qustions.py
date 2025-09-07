#Create a students class then takes of subject as argument in constructor then create a methods to print average 
#code 
class students:
	def __init__(self,name,marks):
		self.name = name
		self.marks = marks
	def get_avg(self):
		sum = 0
		for val in self.marks:
			sum += val
		print("Hi",self.name,"Your score is",sum/3)
s1 = students("Khalid",[80,90,57])
s1.get_avg() 
#
#Create a account cats with 2 attribute - balance and account no
#Create 
class account:
	def __init__(self,bal,acc_no):
		self.bal = bal
		self.acc_no = acc_no
	def debits(self,ammount):
		self.bal -= ammount
		print("BAT",ammount,"Was debited")
		print("Total balance = ",self.get_bal())
		
	def cradits(self,ammount):
		self.bal += ammount
		print("BAT",ammount,"Was creadited")
		print("Total balance = ",self.get_bal())
		
	def get_bal(self):
		return self.bal
		
acc1 = account(10000,123)
acc1.debits(100)
acc1.cradits(500)