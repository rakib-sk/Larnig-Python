# Notes
# Python Complete Notes – Strings, Conditions, Loops, OOP, File Handling, Lists, Tuples, Dictionaries & Sets

এই README.md তে তোমার কোডে ব্যবহৃত **সব Function, Method, Concept**–এর সহজ ব্যাখ্যা দেওয়া আছে।

---

# ✅ String Section

### **Concatenation**
```python
str1 = "Hello"
str2 = " World"
str3 = str1 + str2
```
**কাজ:** দুই বা তার বেশি string যোগ করা।

---

### **len()**
```python
length = len(str3)
```
**কাজ:** string এর length গণনা করে।

---

### **Indexing**
```python
indx = str3[6]
```
**কাজ:** নির্দিষ্ট index-এর character access করা।

---

### **Slicing**
```python
sli = str3[0:2]
```
**কাজ:** index range অনুযায়ী substring বের করা।

---

### **endswith()**
```python
newStr.endswith("per")
```
**কাজ:** string-এর শেষ অংশ চেক করে মিললে True দেয়।

---

### **capitalize()**
```python
newStr.capitalize()
```
**কাজ:** প্রথম অক্ষর uppercase করে।

---

### **replace(old,new)**
```python
newStr.replace("o","a")
```
**কাজ:** একটি string অন্য string দিয়ে replace করা।

---

### **count()**
```python
count_string.count("$")
```
**কাজ:** string-এর মধ্যে কোন char কয়বার আছে তা গোনা।

---

# ✅ Conditional Statements

### if/elif/else
```python
if marks >= 90:
    ...
elif marks >= 80:
    ...
else:
    ...
```
**কাজ:** বিভিন্ন শর্ত অনুযায়ী বিভিন্ন output দেওয়া।

---

# ✅ Input & Type Conversion
```python
a = int(input("Enter num: "))
```
**কাজ:** input নেওয়া → integer-এ convert করা।

---

# ✅ OOP (Object-Oriented Programming)

## Class & Object
```python
class student:
    name = "Zehad"
s1 = student()
```

---

## __init__()
```python
class friends:
    def __init__(self, name, gpa):
        self.name = name
```
**কাজ:** object তৈরি হওয়ার সময় initialize করে।

---

## Methods
```python
def wel_msg(self):
    print("Welcome")
```

---

## Static Method
```python
@staticmethod
def start():
    print("Started")
```
**কাজ:** self ছাড়া method চালানো যায়।

---

## Private Attribute
```python
self.__acc_pass
```
**কাজ:** বাইরে থেকে access করা যায় না।

---

## Inheritance
```python
class TyotaCar(car):
```
**কাজ:** parent class-এর feature child class পায়।

---

## Multilevel Inheritance
```python
class Fortuner(TyotaCar):
```

---

## Multiple Inheritance
```python
class C(A,B):
```

---

## super()
```python
super().__init__(type)
```
**কাজ:** parent constructor call করা।

---

## Polymorphism & Dunder method (__add__)
```python
def __add__(self,num):
    return complex(...)
```
**কাজ:** object add করা → operator overloading।

---

# ✅ Loops

## While Loop
```python
while count <= 5:
```

---

## break
```python
if i == 5:
    break
```

---

## For Loop
```python
for val in nums:
```

---

## range()
```python
range(start, stop, step)
```

---

## pass
```python
pass
```

---

# ✅ List

```python
marks = [20,40,100]
```

## List Methods
### append()
```python
marks.append(20)
```

### sort()
```python
marks.sort()
```

### sort(reverse=True)
```python
marks.sort(reverse=True)
```

### reverse()
```python
marks.reverse()
```

### insert()
```python
marks.insert(1,3)
```

### remove()
```python
marks.remove(20)
```

### pop()
```python
marks.pop(2)
```

---

# ✅ Tuple
```python
tup = (1,2,3)
```

### index()
```python
tup.index(2)
```

### count()
```python
tup.count(2)
```

---

# ✅ File Handling

### open("file","r")
```python
f = open("file.txt","r")
```
**কাজ:** file read করা।

### read()
```python
f.read()
```
**কাজ:** সব ডেটা পড়া।

### readline()
```python
f.readline()
```
**কাজ:** এক লাইন পড়া।

### write()
```python
file.write("text")
```

### Modes
- `"r"` → read  
- `"w"` → write (পুরোনো ডেটা মুছে দেয়)  
- `"a"` → append  
- `"r+"` → read + write  

### with open()
```python
with open("file.txt","r") as f:
```
**কাজ:** file auto close হয়।

---

# ✅ Dictionary

```python
info = {"name":"Rakib","age":17}
```

### Access
```python
info["name"]
```

### Modify
```python
info["age"] = 18
```

### Add new key-value
```python
info["surname"] = "Zehad"
```

### keys()
```python
info.keys()
```

### values()
```python
info.values()
```

### items()
```python
info.items()
```

### get()
```python
info.get("name")
```
**কাজ:** key না থাকলে error না দিয়ে None দেয়।

### update()
```python
students.update(new_dict)
```

---

# ✅ Set

```python
collection = {1,2,3}
```

### add()
```python
set.add(3)
```

### remove()
```python
set.remove(3)
```

### pop()
```python
set.pop()
```

### clear()
```python
set.clear()
```

### union()
```python
set1.union(set2)
```

### intersection()
```python
set1.intersection(set2)
```

### Empty Set
```python
s = set()
```

---

# 🎉 END
এটাই তোমার সম্পূর্ণ README.md, সব ব্যাখ্যাসহ।
