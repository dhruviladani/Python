
#Prime Number

num = 23
# ans = ""
# if(n == 2 or n == 1):
#     ans = "Prime"
# else:
    # for i in range(2, n+1):
    #     if(i % 2 != 0 and n % 2 != 0) :
    #         print(i)
    #         if(n % i == 0 and i != n):
    #             print(i)
    #             ans = "not Prime"
    #             break
    #         else:
    #             ans = "Prime"
    #             break
    #     else:
    #         ans = "NOT prime"
    
# print(ans)

if (num > 1):
    
    for i in range(2, num):
        if(num % i == 0):
            print("not prime")
            break
    else:
        print("prime")

else:
    print("not prime")
