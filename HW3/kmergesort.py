import heapq

def kwaymersort(li,k):
    if len(li) == 1 or li == []:
        return li
    parts = int(round(len(li)/k)) # use it in Windows
#     parts = len(li)/k # use it in Ubuntu
    first = li[:parts]
    second = li[parts:parts*2]
    third = li[parts*2:]
    first.sort()
    second.sort()
    third.sort()
    m = []
    return merge(first,second,third,m)
    
def merge(f,s,t,m,heap = []):
    while len(f) + len(s) + len(t) != 0:
        if len(f) > 0 and f[0] not in heap:
            heapq.heappush(heap, f[0])
        if len(s) > 0 and s[0] not in heap:                
            heapq.heappush(heap, s[0])
        if len(t) > 0 and t[0] not in heap:
            heapq.heappush(heap, t[0])
        heapq.heapify(heap)
        var = heapq.heappop(heap)
        if var in f:
            f.remove(var)
        elif var in s:
            s.remove(var)
        elif var in t:
            t.remove(var)
        m.append(var)
    if len(heap) < 3:
        while heap:
            m.append(heapq.heappop(heap))
        return m
    
li = [4,1,5,2,6,3,7,0]
k = 3

print(kwaymersort(li,k))