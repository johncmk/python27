cache = {0:0,1:0}
cache2 = {0:0,1:0}

'''Time Complexity O(n) b/c it's iterating n time'''

'''DP version topDown, No consecutive 0s'''
def num_no(n,a = 2,b = 1,i =2):
    if n <= 1:
        return 0
    if i == n:
        return a+b
    temp,a = a,a+b
    b = temp
    cache[n] = num_no(n,a,b,i+1)
    return cache[n]

'''DP version bottom up, No consecutive 0s'''
def num_no2(n,a = 2,b = 1,i =2):
    if n <= 1:
        return 0
    while i <= n:
        if i > n:
            break
        temp,a = a,a+b
        b = temp
        cache[i] = a
        i+=1
    return cache[n]

'''DP version topDown, Yes consecutive 0s'''
def num_yes(n, a = 1, b = 1, i = 2):
    if n <= 1:
        return 0
    cache2[n] = pow(2,n) - num_no(n)
    return cache2[n]

'''DP version bottom up, Yes consecutive 0s
There isn't necessary of iteration once the power of 2^n is defined'''
def num_yes2(n, a = 1, b = 1, i = 2):
    if n <= 1:
        return 0
    cache2[n] = pow(2,n) - num_no(n)
    return cache2[n]

print(num_no(4))
print(num_yes(4))
