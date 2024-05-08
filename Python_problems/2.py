def los(a):
    S = set() # declaring a set 
    l = 0           #
    res = 0
    for r in range(len(a)):
        while a[r] in S:
            S.remove(a[l])
            l+=1
        S.add(a[r])
        if len(S) > re  s:
            res = len(S)
    return res        

a = "abcabcbb"
print(los(a))            

"""
As we cannot check each and every substring of the actual string we have to use 2 pointer sliding window method, So each and every
substring will be saved till it encounters repetition of the character. As it shouldn't contain the repeated characters, we can use sets.
So the maximum length that the set reaches will be the length of longest substring 

"""



        