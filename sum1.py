target = 10
arr = [1, 2, 3, 4, 6]

#The Worst type of so0lution
#Time Complexity : O(N^2)
#Space Complexity: O(N)

def FindSum(arr,target):
    result=[]
    for x in range(0, len(arr)):
        for y in range(x + 1, len(arr)):
            if (arr[x] + arr[y] == target):
                if arr[x] > arr[y]:
                    result.append(arr[y])
                    result.append(arr[x])
                else:
                    result.append(arr[x])
                    result.append(arr[y])
    return result


#Testing the method

target = 10
arr = [1, 2, 3, 4, 6]
print(FindSum(arr,target))

