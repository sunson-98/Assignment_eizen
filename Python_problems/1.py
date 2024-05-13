def check(a):
    i = 1
    c = 0
    while(i<len(a)):
        if(a[i-1]>=a[i]):
            c+=1
            if(i>1 and a[i-2] >= a[i]):
                a[i] = a[i-1]
        i+=1
    if(c<2):
        return True
    else:
        return False                          
a = [1, 1, 1] 
print(check(a)) 

#when a[i-1] is greater than a[i] the strict incremental might happen by removing a[i] or a[i-1] instead
# We can replace a[i-1] with a[i] so that the second increment will be deciding weather strict incremental will be possible or not
