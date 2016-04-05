def _shortest(tree,x,y):
    '''return(dep_x,dep_y)'''
    if tree is None:
        return -1,-1
    ldep_x, ldep_y = _shortest(tree.left,x,y)
    if ldep_x>=0 and ldep_y>=0:
        return ldep_x,ldep_y
    rdep_x,rdep_y = _shortest(tree.right,x,y)
    if rdep_x >= 0 and rdep_y >=0:
        return rdep_x and rdep_y
    return (max(ldep_x,rdep_x) + 1 if ldep_x*rdep_x <=0 else 0 if tree is x else -1, max(ldep_y,rdep_y)+1 if ldep_y*rdep_y <=0 else 0 if tree is y else -1)
shortest = lambda tree,x,y: sum(_shortest(tree,x,y))
    
class Tree(object):
    __slots__="left","right"
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
        
t = Tree(Tree(),Tree(Tree(None,Tree()),Tree()))
#test cases
print (shortest(t,t.right.left.right,t.left))
print (shortest(t, t.right.left.right, t.right.right))
print (shortest(t,t.right.left.right,t.right))#lca==y
print (shortest(t,t.right.left,t.right.left)) # same 