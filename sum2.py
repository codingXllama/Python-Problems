def sum(arr, target):
    soln=[]
    for x in range(0, len(arr)):
        for y in range(x + 1, len(arr)):
            if (arr[x] + arr[y]==target) and arr[x] > arr[y]:
                return [arr[y],arr[x]]
            elif (arr[x] + arr[y] == target) and arr[x] < arr[y]:
                return [arr[x], arr[y]]

arr=[8,1,2,3]
print(sum(arr,10))