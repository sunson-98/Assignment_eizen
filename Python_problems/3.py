def check_double(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[j] == 0):
                j+=1
            if(j<len(a) and a[i] == 2 *a[j]):
                return True
    return False

a = [3, 1, 7, 11]
print(check_double(a))    

"""
Each element will be traversing the entire array looking for the double of that element if it finds it will return true, else it will 
return false

I have just applied Brute-force method as I am not familiar with Hash in python

"""
