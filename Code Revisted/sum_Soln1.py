`#Finding the 2 values in a given list that will return the given target sum if possibleq

#Time Complexity : O(n^2)
#Space Complexity: O(n)
def FindSum(arr,target):
    soln=[]
    for x_value in range(0,len(arr)):
        for y_value in range(x_value+1,len(arr)):
            soln.append(x_value)
            soln.append(y_value)
    return soln

print(FindSum([1,3,2,5],7))u