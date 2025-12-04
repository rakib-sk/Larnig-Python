''' 1. 🌦 Weather Analyzer
 এক সপ্তাহের তাপমাত্রা লিস্ট দেওয়া থাকবে।
Loop ব্যবহার করে:
- গড় তাপমাত্রা বের করো
- সবচেয়ে বেশি ও সবচেয়ে কম বের করো
'''

temp = [30,40,25,32,35,38,31]

#Thik 0 max and min temprature
max_temp = temp[0]
min_temp = temp[0]
avarage_temp = 0

i=0
while i<len(temp):
    avarage_temp = temp[i] + temp[i]/2
    
    if max_temp < temp[i]:
        max_temp = temp[i]
        
    if min_temp > temp[i]:
        min_temp = temp[i] 
        
    i += 1
print("Avarage temprature is: ", avarage_temp)    
print("Max temprature is: ", max_temp)
print("Min temprature is: ", min_temp)