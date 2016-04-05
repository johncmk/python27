def mergesort(li):
    if len(li) == 1:
        return li
    from math import floor
    m = floor(len(li)/2)
    r = mergesort(li[m:])
    l = mergesort(li[:m])
    m= []
    return merge(l,r,m)
    
# def merge(l,r):
#     print(l,r)
#     m = []
#     i,a,b = 0,0,0
#     while(len(l)+len(r) > i):
#         if a == len(l):
#             m.append(r[b])
#             b+=1
#         elif b == len(r):
#             m.append(l[a])
#             a+=1
#         elif l[a] >= r[b]:
#             m.append(r[b])
#             b+=1
#         elif l[a] <= r[b]:
#             m.append(l[a])
#             a+=1
#         i+=1
#     return m
        
# def merge(l,r):
#     print(l,r)
#     m = []
#     while(len(l)+len(r) != 0):
#         if 0 == len(l):
#             m.append(r.pop(0))
#         elif 0 == len(r):
#             m.append(l.pop(0))
#         elif l[0] >= r[0]:
#             m.append(r.pop(0))
#         elif l[0] <= r[0]:
#             m.append(l.pop(0))
#     return m        
     
# def merge(l,r,m):
#     print(l,r)
#     if(len(l)+len(r) != 0):
#         if 0 == len(l):
#             m.append(r.pop(0))
#         elif 0 == len(r):
#             m.append(l.pop(0))
#         elif l[0] >= r[0]:
#             m.append(r.pop(0))
#         elif l[0] <= r[0]:
#             m.append(l.pop(0))
#         return merge(l,r,m)
#     else:
#         return m
        
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
print(mergesort(li))