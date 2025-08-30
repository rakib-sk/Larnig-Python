#String part
#Basics Options
#Concatenate
str1 = "Hello"
str2 = " World"
str3 = str1 + str2
#Print str length
length = len(str3)
print(str3,"length of the string ",length)



#indexing 
#calculate indexing
indx = str3[6]
print(indx)


#sliceing
sli = str3[0:2]
print(sli)


#string Functions
#str3.endswith("taxt") চেক করবে লাস্টের সাথে যোদি str এর মিল আছে কি। থাকলে True না থাকলে False

newStr = "i am a web developer"
print(newStr.endswith("per"))
#capitalize এর কাজ প্রথম একটা বড় হাতের করবে।
print(newStr.capitalize())

#replace(new,old) এটি দিয়ে একটি str দিয়ে অন্য str কে রিপলেস করা যায়।

print(newStr.replace("o","a"))

#Pratice qustions
#WAP to input user's fast name. and print length.
fast_name = input("Enter your name:")
fast_name_length = len(fast_name)
print(fast_name_length)

#Partice qustions2
#WAP to find the occurrence of '$' in a string
count_string = " $ is emotion in evary man. \n Time is $"
print(count_string.count("$"))










#Conditional stetment
# student এর মাক ইনপুট দিলে গ্রেড বলবে।
#student_marks = int(input("Enter your mark: "))
if student_marks >= 90:
  print(student_marks,"You have done A")
elif student_marks >= 80:
    print(student_marks,"Your grade is B")
elif student_marks >= 70:
    print(student_marks,"Your grade is C")
elif student_marks >= 60:
    print(student_marks,"Your grade is D")
elif student_marks >= 50:
    print(student_marks,"Your grade is E")
else:
   print("Faill!!!")
   
   
   
   
#Pratice qustions3

#
