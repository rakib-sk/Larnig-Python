#store following word meanig in a python dictionary 
word = {
	"table" : ["a pice of farniture","lisd of fact and figure"],
	"cat" : "a small animal"
}
print(word)
#
#You are given a list of subject of students . Assume one classroom is required  for 1 subject how many classroom 
subject = {"python","java","c++","python","javascript","java","javascript","python","java","c++","c"}
#simple find classroom 
print("we need classroom",len(subject))

#WAP 3subject mark to user. and store them in dictionary 
marks = {}
phy = int(input("Enter Physics mark: "))
chem = int(input("Enter Chem marks : "))
math = int(input("Enter math mark: "))
marks.update({"sub1" : phy})
marks.update({"sub2" : chem})
marks.update({"sub3" : math})
print(marks)
#Figure out a way to store 9 and 9.0 value in the set (you can use take built-in ddatatype
set1 = { 
	("int", 9),
	("float", 9.0)
}
print(set1)
