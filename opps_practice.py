class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = circle(21)
print(c1.area())
print(c1.perimeter())



#####

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role  
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

e1 = Engineer("Elon Musk", 40)  
e1.showDetails()



#####
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price

o1 = Order("chips", 20)
o2 = Order("coffee", 30)

print(o1 > o2)