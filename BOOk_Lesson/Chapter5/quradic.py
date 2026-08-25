import cmath
# Px**2 + qx + r = 0
P = int(input("Enter P: "))
Q = int(input("Enter Q: "))
R = int(input("Enter R: "))

D = Q**2 - (4 * P * R)#b**2 - 4a*c

x1 = (-Q + cmath.sqrt(D)) / (2 * P)
x2 = (-Q - cmath.sqrt(D)) / (2 * P)

print(f"(x1,x2) = ({x1,x2})")