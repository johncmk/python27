import random

def _quickfind(array,x,k):
    p = random.randint(0,len(array)-1)
    array[0], array[p] = array[p],array[0]
    pivot = array[0]
    left = [y for y in array if y < pivot]
    right = [y for y in array[1:] if y >= pivot]
    if k <= len(left):
        return _quickfind(left,x,k)
    elif k == len(left)+ 1:
        return left+[pivot]
    return left + [pivot] + _quickfind(right,x,k-len(left)-1)
    
def quickfind(a,x,k):
    return [v for(_,v) in _quickfind([(abs(y-x),y) for y in a],x,k)]
    
print(quickfind([4,1,3,2,7,4], 5.2, 2))
print(quickfind([4,1,3,2,7,4], 6.5,3))