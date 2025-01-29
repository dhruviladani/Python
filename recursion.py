

# def recursion(n):
#     if (n == 0):
#         return
#     print(n)
#     recursion(n-1)

# recursion(5)



#sum of first n natural numbers

# def sum(n):
#     if (n == 0):
#         return 0
    
#     return n + sum(n-1)

# print(sum(10))


#print all elements in a list
l = [1,2,3,4,5]
def ele(l,i):
    if (i == len(l)):
        return
    print(l[i])
    ele(l,i+1)


ele(l,0)
