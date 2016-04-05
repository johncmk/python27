'''
Created on Sep 15, 2014

@author: John
'''
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
        
k = 7
l = [2,6,5,1,4,9,3]
print(qselect(4, [11, 2, 8, 3]))