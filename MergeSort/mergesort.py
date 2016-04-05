def mergesort(li):
    if len(li) == 1:
        return li
    m = int(len(li)/2)
    l = li[:m]
    r = li[m:]
    leftSub = mergesort(l)
    rightSub = mergesort(r)
    m= []
    return merge(leftSub,rightSub,m)

def merge(l,r,m):
    if(len(l)+len(r) != 0):
        if 0 == len(l):
            m.append(r.pop(0))
        elif 0 == len(r):
            m.append(l.pop(0))
        elif l[0] >= r[0]:
            m.append(r.pop(0))
        elif l[0] <= r[0]:
            m.append(l.pop(0))
        return merge(l,r,m)
    return m        
        
# li = [6,1,5,2,4,3,0]        
li = [6,5,3,1,8,7,2,4,3]
# li = [3,1,4,2]
print(mergesort(li))
