class acc:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #__acc_pass is now privat 

    def reset_pass(self):
        print(self.__acc_pass)

    def __hello(self): #private
        print("hello")

    def welcome(self):
        self.__hello()

acc1 = acc("123", "abc")

print(acc1.acc_no)
print(acc1.reset_pass())
print(acc1.welcome())
