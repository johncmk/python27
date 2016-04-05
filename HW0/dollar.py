# #HW0
# def prepareDictionary(dictionary):
#     for key in range(97,123):
#         dictionary[chr(key)] = (key-96)
# 
# def dollarWords(inputFile,outputFile,dictionary):
#     dollar = 0
#     with open(outputFile,"w") as writeFile:
#         with open(inputFile,"r") as readFile:
#             for line in readFile:
#                 for ch in line.lower():
#                     if ch in dictionary.keys(): 
#                         dollar += dictionary[ch]
#                         if dollar == 100:
#                             writeFile.write(line)
#                 dollar = 0
#             
# dict = {}  # @ReservedAssignment
# prepareDictionary(dict)
# dollarWords("input.txt","output.txt",dict)
