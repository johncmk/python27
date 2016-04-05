def mergeSort(li,count = 0):
    print("mergesort start")
    from math import floor
    if li == []:
        return []
    if len(li) <= 1:
        return li
#     print("count")
    m = floor(len(li)/2)
    count+=1
    r = mergeSort(li[m:], count)
    l = mergeSort(li[:m], count)
#     return l+r
#     print("before")
#     if r != None and l != None:
#         print("after")
#         return foo(l,r)
    print("function call#",count,"r: ",r)
    print("function call#",count,"l: ",l)
    print("return to merge")
    return merge(l,r)
#     print("r: ",r)
#     print("l: ",l)
#     if r > l:
#         return l+r
#     if r < l:
#         return r+l

def merge(l,r):
    print("merge start")
    print("r: ",r)
    print("l: ",l)
    return l+r
    
# li = [6,5,3,1,8,7,2,4,3]
# print(mergeSort(li))


li2 = [1,2,3,4]
li3 = mergeSort(li2)

