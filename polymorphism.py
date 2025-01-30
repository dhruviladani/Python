class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):  # Dunder function
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal, newimg)
    
    def __sub__(self, num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return complex(newreal, newimg)
    
num1 = complex(1,3)
num1.showNumber()

num2 = complex(4,6)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()