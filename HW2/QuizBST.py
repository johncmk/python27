class tree(object):
    __slots__ = "root left right".split()
    def __init__(self,root,left=None,right=None):
        self.root = root
        self.left = left
        self.right= right

def printTree(t,lev= 0):
    if t is None:
        return None
    else:
        print("\t"*lev,t.root)
        return printTree(t.left,lev+1),t.root,printTree(t.right,lev+1)

def _searchTree(t,x):
    if t is None:
        return t
    if x < t.root:
        return _searchTree(t.left,x)
    if x > t.root:
        return _searchTree(t.right,x)
    if x == t.root:
        return t

def searchTree(tree,find):
    if _searchTree(tree, find) is None:
        return False
    return True

def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

#preorder
def preorder(t,lev = 0):
    if t == []:
        return []
    left,node,right = t
    print("\t" * lev, node )
    return preorder(left, lev+1) + [node] + preorder(right,lev+1)

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

def _longest(tree):
    if tree == []:
        return 0,-1
    left,root,right = tree
    l1, d1 = _longest(left)
    l2, d2 = _longest(right)
    return max([d1+d2+2,l1,l2]), max(d1,d2)+1    
       
longest = lambda tree: _longest(tree)[0]

           
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
    
def qselectBST(index,tree):
    print("Before tree == []: ",tree)
    if tree == []:
        print("if the tree == []: ",tree)
        print("return 0, None")
        return 0,None
    left,root,right = tree
    print("---left: ",left)
    print("---root: ",root)
    print("---right: ",right)
    num,x = qselectBST(index,left)
    print("num,x = qselectBST(index,left)")
    print("index: ",index)
    print("num: ",num)
    print("x: ",x)
    if index <= num:
        print("if index <= num:")
        print("return index, x ",index, ",",num)
        return index,x
    if index == num+1:
        print("if index == num+1:")
        print("return index, root ",index,",", root)
        return index,root
    print("num2,y = qselectBST(index-num-1,right)")
    print("index-num-1: ",index-num-1)
    print("right: ",right)
    print("root: ",root)
    num2,y = qselectBST(index-num-1,right)
    print("num: ",num)
    print("num2: ",num2)
    print("y: ",y)
    print("return num+num2+1,y ", num+num2+1,",",y)
    return num+num2+1,y
           
           
           
           
           
li = [4,2,6,3,5,7,1,9]
li1 = [2]
li2 = [2,1,4,3,7,6,9]
li3 = [5]
li4 = [2]

liTree = sort(li)
li1Tree = sort(li1)
li2Tree = sort(li2)
li3Tree = sort(li3)
li4Tree = sort(li4)

# preOrder(liTree)
print(longest(liTree)) 


insert(li3Tree, 6)
insert(li3Tree, 1)
insert(li3Tree, 4)
insert(li3Tree, 3)

insert(li4Tree,1)
insert(li4Tree,3)
insert(li4Tree,4)

# print(li4Tree)
# preorder(li4Tree)
# print(qselectBST(3,li4Tree))

# sampleTree = tree(5,tree(3,tree(2),None),tree(7,tree(6),tree(8)))
 
# printTree(sampleTree)
# print(searchTree(sampleTree, 11))
