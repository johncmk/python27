def printList(li):
    print(li)

def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def qsort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return qsort(left) + [pivot] + qsort(right)    

#preorder
def printTree(t,lev = 0):
    if t == []:
        return []
    left,node,right = t
    print("\t" * lev, node )
    return printTree(left, lev+1) + [node] + printTree(right,lev+1)

def search(tree,find):
    if _search(tree, find) == []:
        return False
    return True
    
#inorder   
def sorted(t):
    if t == []:
        return []
    left,node,right = t
    return sorted(left) + [node] + sorted(right)
             
def preOrder(t,lev = 0):
    if t == []:
        return []
    left,root,right = t
    print("\t"*lev, root)
    preOrder(left, lev+1)
    preOrder(right, lev+1)                    
            
def insert(t,find):
    if search(t,find) == False:
        tree = _search(t, find)
        for node in sort([find]):
            tree.append(node)          
        
           
def delete(tree,find):
    if search(tree,find) == True:
        t = _search(tree,find)
        left,node,right = t
        if left == [] and right == []:
            del t[:]           
        elif left != [] and right == []:
            del t[:]
            for el in left:
                t.append(el)
        elif right != [] and left == []:
            del t[:]
            for el in right:
                t.append(el)
        elif left != [] and right != []:
            key = min(sorted(right))
            t[1] = key
            delete(right,key) 


def longest_deepest(tree):
    if tree == []:
        return 0,-1
    left,root,right = tree
    l1, d1 = longest_deepest(left)
    l2, d2 = longest_deepest(right)
    return max([longest_deepest(d1+d2)+2,l1,l2]), max(longest_deepest(d1,d2))+1           
           
           
def _search(t,x):
    if t == []:
        return t
    l,n,r = t
    if x < n:
        return _search(l,x)
    if x > n:
        return _search(r,x)
    if x == n:
        return t           
           
li = [4,2,6,3,5,7,1,9]
li1 = [2]
li2 = [2,1,4,3,7,6,9]
li3 = [2,3,1]

liTree = sort(li)
li1Tree = sort(li1)
li2Tree = sort(li2)
li3Tree = sort(li3)

# insert(tree,6.5)
insert(liTree,11)
print(liTree)
printTree(liTree)
delete(liTree,1)
printTree(liTree)
# print(_search(tree,0) == _search(tree,6.5))

li4 = [3,2,1]
li4Tree = sort(li4)
print "li4",li4Tree
