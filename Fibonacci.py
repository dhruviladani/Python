
n = 10 
l = [0, 1]
ele = 0
for i in range(2,n+1):
    ele = l[i-1] + l[i-2]
    
    if(ele < 10):
        l = l + [ele]
        
    else:
        break
print(l)
