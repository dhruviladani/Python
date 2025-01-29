# n = 5 
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i

# print(fact)


#Recursion 

def factorial(n):
    if(n == 1):
        return 1
    
    return n * factorial(n-1)
 
print(factorial(5))
