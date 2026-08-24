import cmath

def calculateTriangleArea(a,b,c):
    s = (a + b + c)/2
    area = cmath.sqrt(s*(s-a)*(s-b)*(s-c))

    return area

print(calculateTriangleArea(2,3,4))