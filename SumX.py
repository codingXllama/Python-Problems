arr = [1, 2, 3, 4]
target = 5


def sumX(arr, target):
    nums = {}
    
    for x in arr:
        possibleVal = target - x
        if possibleVal in nums:
            return [possibleVal, x]
        else:
            nums[x] = 1
    return []


print(sumX(arr,target))