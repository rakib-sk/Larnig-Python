f1 = 0
f2 = 1
i = 2
fibonacci = 1
n = int(input("ENter n: "))
while i < n:
    fibonacci = f1 + f2
    f1 = f2 
    f2 = fibonacci

    print(fibonacci)
    i += 1

# 1 2 3 5 8
# 0 + 1 = 1, 1 + 1 = 2, 2+3 = 5, 5+2 = 8 , 8 + 5 = 13 .....