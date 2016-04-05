class Tree(object):
    __slots__ = "root left right".split()
    def __init__(self,root,left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
        
def printTree(t,lev= 0):
    if t is None:
        return None
    else:
        print("\t"*lev,t.root)
        return printTree(t.left,lev+1),t.root,printTree(t.right,lev+1)        
        
# def find(t,k,s = set()):
#     if t is None and len(s) == 0:
#         return t
#     if t is None and len(s) >= 1:
#         return min(s)
#     if t.root == k:
#         s.add(0)
#         return min(s)
#     if t.root > k:
#         s.add(abs(t.root-k))
#         return find(t.left,k,s)
#     if t.root < k:
#         s.add(abs(t.root-k))
#         return find(t.right,k,s)

def find(t,k,s = None):
    if s is None:
        s = {}
    if t is None and len(s) == 0:
        return t
    if t is None and len(s) >= 1:
        return s[min(s.keys())] # return the node
    if t.root == k:
        return (0,t.root)[0]
    if t.root > k:
        s[t.root-k] = t.root
        return find(t.left,k,s)
    if t.root < k:
        s[abs(t.root-k)] = t.root
        return find(t.right,k,s)
        
t = Tree(5,Tree(3,Tree(2),Tree(4)),Tree(7,Tree(6),Tree(8)))
print(find(t,6.4))