def FindSum(arr, target):
    
    #stroing all the values we traversed through in a dictionary
    nums={}
    
    for val in arr:
        possibleSolution = target - val
        if possibleSolution in nums:
            return [possibleSolution, val]
        else:
            nums[val] = 1

    #Returning a list if we cannot find the values for to a target sum    
    return []


print(FindSum([1,2,5],6))