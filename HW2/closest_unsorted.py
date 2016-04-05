def qselect(k,l):
    mySet = set(l) #convert list to set, therefore no duplicate value exists in the list
    li = list(mySet) #convert the set back to list type with duplication eliminated
    from random import randint
    pivot = li[randint(0,len(li)-1)]
    left = [el for el in li if el < pivot]
    right = [el for el in li if el > pivot]
    if k == len(left)+len([pivot]):
        return pivot
    if k <= len(left):
        return qselect(k, left)
    k = k - len(left) - len([pivot])
    return qselect(k, right)
        
def find(a,x,k):
    li = [abs(x-el) for el in a]
    return [a[li.index(el)] for el in li if el < qselect(k,li)]

li = [4,1,3,2,7,4]
x1 = 5.2
k1 = 2
x2 = 6.5
k2 = 3

print(find(li,x1,k1))
print(find(li,x2,k2))
