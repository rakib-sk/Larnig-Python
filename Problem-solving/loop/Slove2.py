'''2. 📊 Student Pass-Fail Counter
একাধিক স্টুডেন্টের মার্কস ইনপুট দিতে হবে।
Loop ব্যবহার করে:
- কতজন পাশ
- কতজন ফেল
- Highest mark'''

print("When you wen't to stop input marks, type n. ")
student_marks = []

total_pass = 0
total_fail = 0

while True:
    marks = input("Enter marks: ")
    if marks=="n":
        break
        
    student_marks.append(int(marks)) 
    
highest_mark = student_marks[0]
i = 0
while i<len(student_marks):
    if student_marks[i] >= 33:
        total_pass = total_pass + 1
    else:
        total_fail = total_fail + 1
        
    if student_marks[i] > highest_mark:
        highest_mark = student_marks[i] 
        
    i += 1
    
    
print("\nTotal pass students is: ", total_pass)    
print("Total fail students is: ", total_fail)
print("Highest mark is: ", highest_mark)