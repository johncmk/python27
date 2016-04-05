'''Q1'''
def _fib(n,cache = {}):
    if n in cache:
        return n
    cache[n] = 1 if n < 2 else _fib(n-1,cache) + _fib(n-2,cache)
    return cache[n]

'''Q2'''
def longest(tree):
    if tree == []:
        return 0 , -1
    left,root,right = tree
    print("left: ",left)
    print("Root: ",root)
    print("Right: ",right)
    l1,d1 = longest(left)
    print("l1 ",l1)
    print("d1 ",d1)
    l2,d2 = longest(right)
    print("l2 ",l2)
    print("d2 ",d2)
    return max([d1+d2+2,l1,l2]), max(d1,d2)+1



'''Q3b'''
def qselect(index,tree):
    if tree == []:
        return 0,None
    left,node,right = tree
    
    num,x = qselect(index,left)
    if index <= num:
        return index,x
    if index == num+1:
        return index,node
    num2,y = qselect(index-num-1,right)
    return num+num2+1,y

print(_fib(100))