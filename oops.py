# class Student:
#     # def __init__(): #Default Constructor
#     #     pass

#     name = "annymous" # class attribute

#     def __init__(self, name, marks): #Parameterized Constructor
#         self.name = name # obj attr > class attr
#         self.marks = marks
#         print("in __init__()")

#     def welcome(self):
#         print("Welcome")

# s1 = Student("Dhruvi", 99)
# print(s1.name, s1.marks)

# s2 = Student("Other", 80)
# print(s2.name, s2.marks)

# s1.welcome()




class student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

    def avg(self):
        sum  = 0
        for i in self.marks:
            sum += i
        print(self.name, "Your avg score is: ", sum/3)


s1 = student("Dhruvi", [99,98,97])
s1.avg()