def findDuplicate(arr):
    # Write your code here
    a=list(arr)
    s=list(set(a))
    for i in s:
        if a.count(i)==2:
            return i 
    pass

print(findDuplicate([1,2,2,3]))

