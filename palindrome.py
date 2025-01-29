#####Palindrome#####

# l = [1, 4, 4, 1]
l = [1, 'a', 'a', 2]
l2 = []
l2 = list(reversed(l))
print(l2)
if(l == l2) :
    print('Palindrom')
else: 
    print('Not Palindrome')



#2nd method 


l = [1, 'a', 'a', 2]
l2 = l.copy()
l2.reverse()
print(l2)
if(l == l2) :
    print('Palindrom')
else: 
    print('Not Palindrome')

