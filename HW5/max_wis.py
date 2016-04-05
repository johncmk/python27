best = {-1:0,0:0}
took = {}

'''Time complexity O(n)'''

'''Top down'''
def max_wis(li): 
    if li == []:
        return 0,[]
    if li == 1:
        return li[0],li
    li.insert(0,0) # prepend dummy node into the list
    return max_wisTopDown(len(li)-1,li),solution(len(li)-1,li)

'''bottom up'''
def max_wis2(li):
    if li == []:
        return 0,[]
    if li == 1:
        return li[0],li
    li.insert(0,0)
    return max_wisBottomUp(len(li),li),solution(len(li)-1,li)
    
def max_wisTopDown(i,li):
    if i in best:
        return best[i]
    best[i] = max(max_wisTopDown(i-1,li),max_wisTopDown(i-2,li)+li[i])
    took[i] = best[i] != best[i-1]
    return best[i]

def max_wisBottomUp(n,li):
    for i in range(1,n):
        best[i] = max(best[i-1],best[i-2]+li[i])
        took[i] = best[i] != best[i-1]
    return sum(solution(n-1,li))

        
def solution(i,li):
    if i <= 0:
        return []
    if took[i]:
        return solution(i-2,li) + [li[i]]
    return solution(i-1,li)        
        
li = [-1,8,10]
print(max_wis(li))
print(max_wis2(li))
