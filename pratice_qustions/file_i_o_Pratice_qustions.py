#Create a new file "pratice.txt" using python add following data
with open("pratice.txt","w") as f:
	f.write("Hi everyone \n we are larning file i \n using Java I Like programming in Java") 
f.close()
#
#
#WAF that replace all occurrence of "Java" with python file
with open("pratice.txt","r+") as f:
	data = f.read()
	print(data)
new_data = data.replace("Java","Python")
print(new_data)
with open("pratice.txt","w") as f:
	f.write(new_data)
#
#
#Search if word "larnig" exist or not
def check_word():
    with open("pratice.txt", "r") as f:
        data_r_m = f.read()
        word = "larning"
        if data_r_m.find(word) != -1:
            print(word, "is found!")
        else:
            print(word, "is not found")

check_word()
#
#
#WAP to find in which line of the file does the word "learning" occur first print -1 if word not foud
def check_line():
    word = "programming"
    data_file = True
    line_no = 1
    with open("pratice.txt","r") as f:
        while data_file:
            data_file = f.readline()
            if (word in data_file):
                print(word, "is line", line_no)
                return
            line_no += 1
    return -1

check_line()
#
#
#From a file contuining numbars separated by comma,print count even numbars
count = 0
with open("demo.txt","r") as f:
	data = f.read()
	
	nums = data.split(",")
	for val in nums:
		if(int(val)%2 == 0):
			count += 1
print(count)
