#Reccursive approach for computing the fibonacci sequence of a given number

def FibN(n):
    if n<=1:
        return n
    else:
        return FibN(n-1)+FibN(n-2)

#Printing the fibonacci sequence from 0 to 10
for nums in range(0,11):
    print("When n= {}, Fibonacci value is: {}".format(nums,FibN(nums)))