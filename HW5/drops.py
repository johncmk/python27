from math import floor

cache = {(1,1):1}

# def drops(f,eg,breakEg = True,top = 0, mid = 0,ground = 0, trial = 0):
#     if (f,eg) in cache:
#         return cache[(f,eg)]
#     ground = mid
#     mid = floor((f-1)/2)
#     top = mid
#     if breakEg:
#         for i in range(ground,top):
#             trial += 1
#         cache[(top,eg)] = trial
#         return drops((f-top),eg,False)
#     else:
#         return drops((f-top),eg,True)
#     return cache[(f,eg)]


best = {}

'''Top down'''
def drops(n, k):
    if (n,k) in best:
        return best[n,k]
    if k == 1:
        return n
    if n == 0:
        return 0
    best[n,k] = 10000000000000
    s= 0
    for i in range(1,n+1):
        print("i: ",i)
        print("[1] (n,k) s: ",n,k,"",s)
        s = max(drops(n-i,k), drops(i-1,k-1))+1
        print("[2]--- (n,k) s: ",n,k,"",s)
        if s < best[n,k]:
            best[n,k] = s
    return best[n,k]

print(drops(5,2))            
print("best: ",best)