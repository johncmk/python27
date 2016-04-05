'''a) Solution a: using hash table'''
def triplesHash(li, dict = None, lengthEach = None, lengthTotal = None):
    if lengthTotal == 0:
        return [key for key in dict if dict[key] != 0]
    if dict is None:
        dict = {0:0}
        lengthEach = len(li)
        lengthTotal = len(li)
    if len(li) < 2:
        return dict
    if lengthEach == 0:
        li.insert(len(li)-1,li.pop(0))
        lengthEach = len(li)
        lengthTotal -=1
        return triplesHash(li,dict,lengthEach,lengthTotal)
    key = li[0]+li[1]
    if li.count(key) >= 1 and lengthEach > 0 and key not in dict and key <= max(li):
        dict[key] = [li[0],li[1]]
    li.insert(len(li)-1,li.pop(1))
    lengthEach -= 1
    return triplesHash(li,dict,lengthEach,lengthTotal)


'''b) Solution b: without using hash table'''
def triples(li, result = None, lengthEach = None, lengthTotal = None):
    if lengthTotal == 0:
        return result    
    if result is None:
        result = []
        lengthEach = len(li)
        lengthTotal = len(li)
    if len(li) < 2:
        return result
    if lengthEach == 0:
        li.insert(len(li)-1,li.pop(0))
        lengthEach = len(li)
        lengthTotal -=1
        return triples(li,result,lengthEach,lengthTotal)
    key = li[0]+li[1]
    if li.count(key) >= 1 and lengthEach > 0 and key <= max(li) and key not in result:
        result.append(key)
    li.insert(len(li)-1,li.pop(1))
    lengthEach -= 1
    return triples(li,result,lengthEach,lengthTotal)

li = [4,1,3,2,7,4]

print(triplesHash(li))
print(triples(li))
