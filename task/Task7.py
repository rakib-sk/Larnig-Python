
user_list = eval(input("Enter a number list: "))#using eaval to input multipul numnar
#
#create a function name is find_avergage
def find_average(numbers):
    if len(numbers) == 0:# if numbar length == 0
        print("List is empty, average cannot be calculated.")
        return #return function
    total = sum(numbers) #sum() using to print their sum
    
    count = len(numbers) #calculate numabr length
    average = total / count #calculate agarage
   
    print(f"Average of this list, {numbers} is {average}") 

find_average(user_list) #call function