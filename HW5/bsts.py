cache = {0:1}

'''Time Complexity O(n^2)'''

'''Top down'''
def bsts(n):
    if n in cache:
        return cache[n]
    cache[n] = sum(bsts(i-1)*bsts(n-i) for i in range(1, n+1))
    return cache[n]

'''Bottom up'''
def bsts2(n):
    cache = {0: 1}
    for i in range(1, n+1):
        cache[i] = sum(cache[j-1]*cache[i-j] for j in range(1,i+1))
    return cache[n]

print(bsts2(3))
