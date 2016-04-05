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
 
def Findlca(t,a,b):
    if t is None:
        return t
    if t.root > a and t.root > b:
        return Findlca(t.left,a,b)
    if t.root < a and t.root < b:
        return Findlca(t.right,a,b)
    return t
    
def shotest(tree):
    if tree is None:
        return 0, -1
    l1,d1 = shotest(tree.left)
    l2,d2 = shotest(tree.right)
    return max([d1+d2+2,l1,l2]), max(d1,d2)+1    


    
# def lca(t,a,b):
#     if t is None:
#         return False,False,0,-1
#     '''recursively go through trees in left and right side and return from the leaves bottom to top'''
#     dx1,dx2,lcal,lenl = lca(t.left,a,b)
#     if dx1 and dx2:
#         return dx1,dx2,lcal,lenl
#     dy1,dy2,lcar,lenr = lca(t.right,a,b)
#     if dy1 and dy2:
#         return dy1,dy2,lcar,lenr
#     '''if a and b are found in either left sub tree or right subtree 
#         then return the length of either left or right from where its found
#     '''
#     if (dx1 and dy2) or (dx2 and dy1):
#         return True,True,t.root,lenl+lenr
#     elif dx1 and dx2:
#         return dx1,dx2,lcal,lenl
#     elif dy1 and dy2:
#         return dy1,dy2,lcar,lenr
#     '''if a is in right side of either left or right subtree
#     elif b is in left side of either left or right subtree
#     elif a is found not in right side of either left or right subtree
#     elif b is found not in left side of either left or right subtree'''
#     if a == t.root and dy2 or dx2:
#         return True, True,t.root,max(lenr,lenl)
#     elif b == t.root and dy1 or dx1:
#         return True, True,t.root,max(lenr,lenl)
#     elif a == t.root and not(dy2 and dx2):
#         return True, False, None, 1
#     elif b == t.root and not(dx1 and dy1):
#         return False, True, None, 1
#     '''is LCA is found in either left side or right side of the subtree'''
#     if (dx1 and not dx2) or (not dx1 and dx2):
#         return dx1,dx2,None,lenl+1
#     elif(dy1 and not dy2) or (not dy1 and dy2):
#         return dy1,dy2,None,lenr+1
#     
#     return False,False,0,-1
    
def lca(t,a,b):
    if t is None:
        return False,False,0,-1
    dx1,dx2,lcal,lenl = lca(t.left,a,b)
    if dx1 and dx2:
        return dx1,dx2,lcal,lenl
    dy1,dy2,lcar,lenr = lca(t.right,a,b)
    if dy1 and dy2:
        return dy1,dy2,lcar,lenr
    if (dx1 and dy2) or (dx2 and dy1):
        return True,True,t.root,lenl+lenr
    elif dx1 and dx2:
        return dx1,dx2,lcal,lenl
    elif dy1 and dy2:
        return dy1,dy2,lcar,lenr
    if a == t.root and dy2 or dx2:
        return True, True,t.root,max(lenr,lenl)
    elif b == t.root and dy1 or dx1:
        return True, True,t.root,max(lenr,lenl)
    elif a == t.root and not(dy2 and dx2):
        return True, False, None, 1
    elif b == t.root and not(dx1 and dy1):
        return False, True, None, 1
    if (dx1 and not dx2) or (not dx1 and dx2):
        return dx1,dx2,None,lenl+1
    elif(dy1 and not dy2) or (not dy1 and dy2):
        return dy1,dy2,None,lenr+1
    
    return False,False,0,-1    

sampleTree = tree(5,tree(3,tree(2)),tree(7,tree(6),tree(8)))
 
print("Shortest Path in 2 recursions ",shotest(Findlca(sampleTree,6,8))[0])
print("Shortest Path in 1 recursion ",lca(sampleTree,6,8)[3])
