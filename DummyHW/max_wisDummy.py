a = [0,7,8,5]
n = len(a) #4
best = {-1:0,0:0}
took = {}

def topDown(i):
#     print("a[i]: ",a[i])
    if i in best:
        return best[i]
    best[i] = max(topDown(i-1),topDown(i-2)+a[i])
    took[i] = best[i] != best[i-1]
    return best[i]

def bottomup(n):
    for i in range(1,n):
        best[i] = max(best[i-1],best[i-2]+a[i])
        took[i] = best[i] != best[i-1]
    return solution(n-1)

        
def solution(i):
    if i <= 0:
        return []
    if took[i]:
        return solution(i-2) + [a[i]]
    return solution(i-1)

print("topDown: ",topDown(n-1))
print("bottomUp: ",bottomup(n))
print("solution: ",solution(n-1))
print("best: ",best)
print("took: ",took)