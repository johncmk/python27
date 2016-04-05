import random
## cannot maintain the order of elements in original array

def quickfind(array,x,k):
    print("array: ",array)
    if k < 0 or k > len(array):
        print("error")
        return
    pivot = array[random.randint(0,len(array)-1)]
    print("pivot: ",pivot)
    realpivot = abs(pivot-x)
    print("realpivot: ",realpivot)
    left = []
    right = []
    equal = []
    for m in array:
        print("for m in array:")
        if abs(m-x) < realpivot:
            print("abs(m-x) < realpivot: ")
            print("left Append: ",abs(m-x))
            left.append(m)
        elif abs(m-x) > realpivot:
            print("abs(m-x) > realpivot: ")
            print("right Append: ",abs(m-x))
            right.append(m)
        else:
            print("abs(m-x) == realpivot: ")
            print("equal Append: ",abs(m-x)) 
            equal.append(m)
     
    print("left: ",left)
    print("right: ",right)
    print("equal: ",equal)
    if k <= len(left):
        print("k <= len(left): ")
        print(left)
        return quickfind(left,x,k)
    if k <= len(left) + len(equal):
        print("k <= len(left) + len(equal):")
        print(left+equal)
        rightLength = k - len(left)
        print("left + equal[k-len(left)]:  " , "len(left)= ",len(left),",","k - len(left)) = ",k - len(left))
        return left+equal[:rightLength]
    return left + equal + quickfind(right,x,k-len(left)-len(equal))


print("Final output where x = 5.2 and k = 2   ",quickfind([4,1,3,2,7,4], 5.2, 2))
print("Final output where x = 6.5 and k = 3    ",quickfind([4,1,3,2,7,4], 6.5,3))