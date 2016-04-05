def find(li,x,k):
    if len(li) == k:
        return li
    m = int(len(li)/2)
    if li.count(li[m]) > k:
        li.remove(li[m])
        return find(li,x,k)
    if li.count(li[m]) == k and len(li) == k+1:
        return find([min(li)]*k,x,k)
    if x > li[m]:
        return find(li[m:],x,k)
    if x < li[m]:
        return find(li[:m],x,k)

li = [1,2,3,4,4,7]
x1 = 5.2
k1 = 2
x2 = 6.5
k2 = 3

print(find(li,x1,k1))
print(find(li,x2,k2))
