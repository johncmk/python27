'''Inversion incomplete!! Not giving right answer when list is [2,4,1,3,5]'''
# def inversions(li,c=[],inv1 = 0,inv2 = 0):
#     if len(li) == 1:
#         return li
#     m = int(len(li)/2)
#     lsub = li[:m]
#     rsub = li[m:]
#     lsub = reBox(lsub,inv1)
#     rsub = reBox(rsub,inv2)
#     total = lsub[1] + rsub[1]
#     c = []
#     return(mergeTwo(lsub[0],rsub[0],c,total))
#      
# #Recursion sorting for left and right sub array
# def reBox(li,inv):
#     if len(li) == 1:
#         return li
#     m = int(len(li)/2)
#     l = li[:m]
#     r = li[m:]
#     c = []
#     return merge(l,r,c,inv)
#    
# #left sub and right sub array sorting        
# def merge(l,r,m,inv):
#     if(len(l)+len(r) != 0):
#         if 0 == len(l):
#             m.append(r.pop(0))
#         elif 0 == len(r):
#             m.append(l.pop(0))
#         elif l[0] >= r[0]:
#             inv +=1
#             m.append(r.pop(0))
#         elif l[0] <= r[0]:
#             m.append(l.pop(0))
#         return merge(l,r,m,inv)
#     return m,inv
#      
# #merge two sorted left and right sub array    
# def mergeTwo(l,r,m,totalInv):
#     while(len(l)+len(r) != 0):
#         if 0 == len(l):
#             m.append(r.pop(0))
#         elif 0 == len(r):
#             m.append(l.pop(0))
#         elif l[0] >= r[0]:
#             totalInv +=1
#             m.append(r.pop(0))
#         elif l[0] <= r[0]:
#             m.append(l.pop(0))
#     return totalInv
# 
# li = [3,1,4,2]
# print(inversions(li))



'''Faisal's version'''
# #inversions counting using mergsort
# inversion = 0
#  
# def merge (left,right):
#     result = []
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#             else:
#                 global inversion
#                 print("len(left): ",len(left))
#                 inversion += len(left)
#                 result.append(right.pop(0))
#         elif len(left) > 0:
#             result += left
#             print("merge(): left: ",left)
#             print("merge(): result: ",result)
#             left = []
#         elif len(right) > 0:
#             result += right
#             right = []
#     return result
#  
#  
# def inversions(list):
#     size = len(list)
#     if size <= 1:
#         return list #consider it sorted
#     mid = int(size / 2)
#     left = list[:mid]
#     right = list[mid:]
#     left = inversions(left)
#     right = inversions(right)
#     print("left: ",left)
#     print("right: ",right)
#     print("inversion: ",inversion)
#     return merge(left,right)
 
'''Inversion fixed 10/29/2014''' 
inversion = 0
def inversions(li):
    if len(li) == 1:
        return li
    m = int(len(li)/2)
    l = li[:m]
    r = li[m:]
    leftSub = inversions(l)
    rightSub = inversions(r)
    m= []
    return merge(leftSub,rightSub,m)

def merge(l,r,m):
    if(len(l)+len(r) != 0):
        if 0 == len(l):
            m.append(r.pop(0))
        elif 0 == len(r):
            m.append(l.pop(0))
        elif l[0] >= r[0]:
            global inversion
            inversion += len(l)
            m.append(r.pop(0))
        elif l[0] <= r[0]:
            m.append(l.pop(0))
        return merge(l,r,m)
    return m        
        
# li = [6,1,5,2,4,3,0]        
# li = [6,5,3,1,8,7,2,4,3]
# li = [3,1,4,2]
# print(inversions(li))
# print("inversion: ",inversion) 
 
li= [3,1,4,2]
# li = [2,4,1,3,5] 
inversions(li)
print(inversion)

    