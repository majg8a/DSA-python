def foo(arr):
    newArr=[]
    for i in range(len(arr)):
        newArr.append(arr[len(arr)-1-i])
    return newArr

print(foo([1,2,3,4,5,6,7,8,9]))