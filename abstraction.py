# class car:

#     def __init__(self):
#         self.a = False
#         self.b = False
#         self.c = False

#     def start(self):
#         self.c = True
#         self.a = True
#         print("started...")

# s = car()
# s.start()



# #practice que

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    def debit(self, amount):
        self.balance -= amount
        print(amount,"/-  debited")
        print("total balance = ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print(amount, "/-  credited")
        print("total balance = ", self.balance)

a = Account(10000, 123)
a.debit(1000)
a.credit(500)
