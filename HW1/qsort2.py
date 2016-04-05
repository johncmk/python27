def BST(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [BST(left)] + [pivot] + [BST(right)]

def qsort(arr):
    if arr == []:
        return []
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return qsort(left) + [pivot] + qsort(right)    

#preorder
def preorder(tree,lev = 0):
    if tree == []:
        return []
    left,node,right = tree
    print("\t" * lev, node )
    return preorder(left, lev+1) + [node] + preorder(right,lev+1)

def search(tree,find):
    if tree == []:
        return False
    left,root,right = tree
    if find < root:
        return search(left,find)
    if find > root:
        return search(right,find)
    if root == find:
        return True
#inorder   
def inorder(tree):
    if tree == []:
        return []
    left,node,right = tree
    return inorder(left) + [node] + inorder(right)
            
def insert(tree,find):
    if tree == []:
            return []
    if search(tree, find) == False:
        left,root,right = tree
        if find < root and left != []:
            return insert(left,find)
        elif find < root and left == []:
            for node in BST([find]):
                left.append(node)
        if find > root and right != []:
            return insert(right,find)
        elif find > root and right == []:
                for node in BST([find]):
                    right.append(node)
           
def delete(tree,find):
    if search(tree,find) == True:
        left,root,right = tree
        if find > root:
            return delete(right,find)
        if find < root:
            return delete(left,find)
        if find == root:
            if left == [] and right == []:
                del tree[:]           
            elif left != [] and right == []:
                del tree[:]
                for el in left:
                    tree.append(el)
            elif right != [] and left == []:
                del tree[:]
                for el in right:
                    tree.append(el)
            elif left != [] and right != []:
                key = min(inorder(right))
                tree[1] = key
                delete(right,key)           

#Kth smallest number in the list           
def qselect(k,l):
    from random import randint
    if k <= 0 or l == []:
        return -1 #print error condition
    else:
        pivot = l[randint(0,len(l)-1)]
        left = [el for el in l if el < pivot]
        right = [el for el in l if el > pivot]
        if k <= len(left):
            return qselect(k, left)
        if k == len(left)+len([pivot]):
            return pivot
        else:
            k = k - len(left) - len([pivot])
            return qselect(k, right)
        
def _search(t,x):
    if search(t,x) == False:
        return []
    l,n,r = t
    if x < n:
        return _search(l,x)
    if x > n:
        return _search(r,x)
    if x == n:
        return t             
           
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

           
li = [4,2,6,3,5,7,1,9]
li1 = [2]
li2 = [2,1,4,3,7,6,9]
li3 = [5]

liTree = BST(li)
li1Tree = BST(li1)
li2Tree = BST(li2)
li3Tree = BST(li3)


# insert(li3Tree,1)

# insert(li3Tree,4)
# insert(li3Tree,3)
# insert(li3Tree,1)
# insert(li3Tree,8)
# insert(li3Tree,6)
# insert(li3Tree,9)



for i in reversed(range(3,5)):
    insert(li3Tree,i)    
    
print(preorder(li3Tree))


print(longest(li3Tree))

liSame = [4,1,3,2,7,4]
print(qsort(liSame))

# k = 7
# l = [2,6,5,1,4,9,3]
# print(2,"th smallest number is the list", qselect(2, [3, 10, 4, 7, 19]))