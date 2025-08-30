#Dictiovalue
# "key" : "value"
info = {
  "name": "Rakib",
  "age" : 17,
  "GPA" : 5.0
}
print(info)
print(type(info))
#Ascces single or multiple value
print(info["name"],info["GPA"])
#Adding new value
info["name"] = "Abdur Rohoman"
info["GPA"] = 4.89
print(info)
#add new kay and value
info["surname"] = "Zehad"
print(info)
#
#
#Nesting Dictionray
students  = {
  "name" : "Khalid",
  "subject":{
    "Chem" : 50,
    "Phy" : 45,
    "Math" : 50
  }
}
print(students["name"])
print(students["subject"])
#
#
#Dictionray methods
#keys methods use to print all key
print(students.keys());
#casting Dictionray
print(type(list(students)))
#
#value methods use to print all values
print(students.values())
#
#items Methods use to print all Dictionray
#
print(students.items())
#
#get Methods use to handle eror
print(students.get("name"))
#
#update Methods use to update Dictionray
#dict_name.update(update_dictionary _name)
new_dict = {
	"name" : "sanjidha",
	"age" : 99
}
add_dict = students.update(new_dict)
print(students)
#
#
#
#Set in python
#How to create Sets
collection = {1,2,3,4}
print(collection)
#print type 
print(type(collection))
#Set এর মধ্য একটা value দুইবার লিখলে ওইটা Ingonre করে 
set_ingore_value = {1,2,3,4,2,2}
print(set_ingore_value)
#length count করার সময় ও Ignore করবে
print(len(set_ingore_value))
# set এর মধ্য string লেখা যায়
string_in_set = {"Rakib","Badho","shoan","Fishan"}
print(string_in_set)
#How to create empty in python
#normally 
empty_set = {} #but this a dictionary not a empty set
#if i print their type to print it dict 
print(type(empty_set))
#So How to create empty set? 
empty_set_check = set()
#This is a empty set
#if i print their type to print it set 
print(type(empty_set_check))
#
#
#Methods in sets 
#add() methods to use add value in set 
empty_set_check.add(3)
empty_set_check.add("Hello")
empty_set_check.add("world")
empty_set_check.add(2)
empty_set_check.add(0)
print(empty_set_check)
#remove() methods to use remove elements in sets 
empty_set_check.remove("Hello")
print(empty_set_check)
#pop() use to remove random value in the set 
empty_set_check.pop()
print(empty_set_check)
#clear() use to create emptyempty
#set.union(set2) এটা দুইটা সেট মিলাইয়ে সাজিয়ে output দিবে কিন্তু একটা value একবার নিবে 
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9} 
new_set = set1.union(set2)
print(new_set)
#set.intersection(set2) সব সেটের মিল গুলো নিবে 
inter_set = set1.intersection(set2)
print(inter_set)
#
#
empty_set_check.clear()
print(empty_set_check)
