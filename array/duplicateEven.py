
def foo(arr: list):
    newArr=[] 
    for i in range(len(arr)):
        if arr[i] % 2==0:
            newArr= newArr + [arr[i],arr[i]] 
        else:
            newArr.append(arr[i])
    return newArr

print(foo([1,2,5,6,8]))

