# Qs1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

# Qs2
class Employee:
    def __init__(self, role, dep, salary):
        self.role = role
        self.dep = dep
        self.salary = salary

    def showDetelis(self):
        print("Role = ", self.role)
        print("dep = ", self.dep)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "40000")

c1 = Engineer("Zehad", 21)
c1.showDetelis()