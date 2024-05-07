def check(a):
    i = 1
    c = 0
    while(i<len(a)):
        if(a[i-1]>=a[i]):
            c = c+1
            if(i>1 and a[i-2] >= a[i]):
                a[i] = a[i-1]
        i += 1    
    return c < 2  
a = [1, 1, 1] 
print(check(a))             