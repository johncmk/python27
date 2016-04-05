import heapq
import sys

# '''User input version'''
# def medians(minH = [],maxH = [],mD = []):
#     for line in sys.stdin:
#         if line == "\n":
#             break
#         else:
#             var = int(line.strip("\n"))
#         if len(minH) + len(maxH) == 0:
#             heapq.heappush(minH,var)
#             heapq.heapify(minH)
#         if mD != []:
#             if var >= mD[len(mD)-1]:
#                 heapq.heappush(minH,var)
#                 heapq.heapify(minH)
#             elif var <= mD[len(mD)-1]:
#                 heapq.heappush(maxH,var)
#                 heapq._heapify_max(maxH)
#         if len(minH) - len(maxH) == 1 :
#             mD.append(minH[0])
#         if len(maxH) - len(minH) == 1:
#             mD.append(maxH[0])
#         if len(minH) == len(maxH) and len(minH) + len(maxH) != 0:
#             mDvar = (minH[0] + maxH[0])/2.0
#             varS = str(mDvar)
#             varLast = int(varS[len(varS)-1])
#             if varLast > 0:
#                 mD.append(mDvar)
#             else:
#                 mD.append(int(mDvar))
#         if abs(len(minH) - len(maxH)) > 1:
#             if len(minH) > len(maxH):
#                 while(len(minH) - len(maxH) != 1):
#                     heapq.heappush(maxH, heapq.heappop(minH))
#                     heapq._heapify_max(maxH)
#             elif len(maxH) > len(minH):
#                 while(len(maxH) - len(minH) != 1):
#                     heapq.heappush(minH,heapq.heappop(maxH))
#                     heapq.heapify(minH)
#     print(mD)
    

'''Non-user input version'''
def medians(li,minH = [],maxH = [],mD = []):
    if len(li) <= 1:
        return li
    while(li != []):
        var = li.pop(0)
        if len(minH) + len(maxH) == 0:
            heapq.heappush(minH,var)
            heapq.heapify(minH)
        if mD != []:
            if var >= mD[len(mD)-1]:
                heapq.heappush(minH,var)
                heapq.heapify(minH)
            elif var <= mD[len(mD)-1]:
                heapq.heappush(maxH,var)
                heapq._heapify_max(maxH)
        if len(minH) - len(maxH) == 1 :
            mD.append(minH[0])
        if len(maxH) - len(minH) == 1:
            mD.append(maxH[0])
        if len(minH) == len(maxH) and len(minH) + len(maxH) != 0:
            mDvar = (minH[0] + maxH[0])/2.0
            varS = str(mDvar)
            varLast = int(varS[len(varS)-1])
            if varLast > 0:
                mD.append(mDvar)
            else:
                mD.append(int(mDvar))
        if abs(len(minH) - len(maxH)) > 1:
            if len(minH) > len(maxH):
                while(len(minH) - len(maxH) != 1):
                    heapq.heappush(maxH, heapq.heappop(minH))
                    heapq._heapify_max(maxH)
            elif len(maxH) > len(minH):
                while(len(maxH) - len(minH) != 1):
                    heapq.heappush(minH,heapq.heappop(maxH))
                    heapq.heapify(minH)
    return mD
     
 
'''Non-User input execution'''    
li = [5,3,4,1,6]
print(medians(li))

# '''User input execution'''
# medians()