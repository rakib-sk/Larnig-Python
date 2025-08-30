#List 
marks = [20,40,100,50,80]
print(marks[1])
print(type(marks))
#val changing
marks[0] = 80
print(marks)
#slice
print(marks[0:2])
#List Methods
#append
marks.append(20)
print(marks)
#short  
srt = marks.sort()
print(marks)
#using reverse = True
marks.sort(reverse = True)
print(marks)
#list reverse Methods
marks.reverse()
print(marks)
#insert Minsert
marks.insert(1,3)
print(marks)
#remove
marks.remove(20)
print(marks)
#pop 
marks.pop(2)
print(marks)

#Touple
tup = (1,2,3,4)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1:3])
#tup = (1) is not allowed
#Touple Methods
print(tup.index(2))
print(tup.count(2))

