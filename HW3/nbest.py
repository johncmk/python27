import time
import heapq
import itertools
import random

'''Help comparison tuples'''
def lessThan(x,pivot):
    return x[0]+x[1] < pivot[0]+pivot[1] or (x[0]+x[1]==pivot[0]+pivot[1] and x[1] < pivot[1])

def greaterThan(x,pivot):
    return x[0]+x[1] > pivot[0]+pivot[1] or (x[0]+x[1]==pivot[0]+pivot[1] and x[1] > pivot[1])

def lessThanEqualTo(x,pivot):
    return x[0]+x[1] <= pivot[0]+pivot[1] or (x[0]+x[1]==pivot[0]+pivot[1] and x[1] <= pivot[1])

def greaterThanEqualTo(x,pivot):
    return x[0]+x[1] >= pivot[0]+pivot[1] or (x[0]+x[1]==pivot[0]+pivot[1] and x[1] >= pivot[1])


'''(a)'''
def qsort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if lessThan(x,pivot)]
    right = [x for x in a[1:]]
    return qsort(left) + [pivot] + qsort(right)

def nbesta(a,b,c=[],d = {}):
    if (a and b) != []:
        for v1 in a:
            for v2 in b:
                d[(v1,v2)] = v1*v2
        for k in d:
            c.append(k)
    return qsort(c)[:4]
    

'''(b)'''
def qselect(k,l):
    from random import randint
    if l == []:
        return l #print error condition
    pivot = l[randint(0,len(l)-1)]
    left = [el for el in l if lessThan(el,pivot)]
    right = [el for el in l if greaterThan(el,pivot)]
    if k <= len(left):
        return qselect(k, left)
    if k == len(left)+len([pivot]):
        return pivot
    k = k - len(left)-len([pivot])
    return qselect(k, right)
    
def nbestb(a,b,c=[],d={}):
    if (a and b) != []:
        for v1 in a:
            for v2 in b:
                d[(v1,v2)] = v1*v2
        for k in d:
            c.append(k)
        pivot = qselect(4, c)
        return [el for el in c if lessThanEqualTo(el, pivot)]

'''(c)'''
def nbestc(a,b,h=[]):
    for i in itertools.product(a,b):
        heapq.heappush(h,(i[0]+i[1],(i[1],i[0])))
    heapq.heapify(h)
    c = []
    while h:
        var = heapq.heappop(h)
        c.append(var[1][::-1])
        if len(c) == 4:
            break
    return c   

# a = [4,1,5,3]
# b = [2,6,3,4]

a = [random.randint(0,5000) for p in range(0,5000)]
b = [random.randint(0,5000) for p in range(0,5000)]

t = time.time()
print(nbesta(a,b))
print(time.time()-t)

t2 = time.time()
print(nbestb(a,b))
print(time.time()-t2)

t3 = time.time()
print(nbestc(a,b))
print(time.time()-t3)