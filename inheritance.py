###single inheritance

class car:

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyota(car):
    def __init__(self, name):
        self.name = name


c1 = Toyota("fortuner")
c2 = Toyota("prius")

print(c1.start())



###Multilevel inheritance


class car:

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyota(car):
    def __init__(self, brand):
        self.name = brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type

c1 = Fortuner("diesel")
c1.start()


###multiple inheritance

class A:
    a = "class A"

class B:
    b = "class B"

class C(A, B):
    c = "class C"

c1 = C()

print(c1.c)
print(c1.a)
print(c1.b)
print("..........")



### super()

class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyota(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        
print("..........")
c1 = Toyota("prius", "electric")
print(c1.type)



##### class methods

class person:
    name = "anonymous"

    def change_name(self, name):
        self.__class__.name = "abc"

    @classmethod
    def change_name(cls, name):
        cls.name = name


p1 = person()
p1.change_name("updated name")
print(p1.name)
print(person.name)



####property

class student:
        def __init__(self, phy, chem, math):
            self.phy = phy
            self.chem = chem
            self.math = math

        # def calcPercentage(self):
        #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

        @property
        def percentage(self):
            return str((self.phy + self.chem + self.math)/3) + "%"
        
s1 = student(78,89,90)
print(s1.percentage)

s1.phy = 92
print(s1.percentage)