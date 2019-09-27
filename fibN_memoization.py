def FibN(n):
    fibN_cache={}
    if n in fibN_cache:
        return fibN_cache[n]
    
    #Computing the fibN
    if n <=1:
        value=n
    else:
        value=FibN(n-1)+FibN(n-2)
    
    fibN_cache[n]=value
    return value


#testing the function
for num in range(0,11):
    print(num,":",FibN(num))