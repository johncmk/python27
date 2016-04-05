#!/usr/bin/python3
#HW0

#Generate dictionary
def prepareDictionary(dictionary):
    for key in range(97,123):
        dictionary[chr(key)] = (key-96)
    return dictionary

#Write output.txt file if word costs a dollar
def dollarWords(inputFile,outputFile,dictionary):
    with open(outputFile,"w") as writeFile:
        with open(inputFile,"r") as readFile:
            for line in readFile:
                dollar = 0
                word = line.lower().strip()
                if len(word) > 4: 
                    for i in range(0,len(word)):
                        if word[i] in dictionary.keys(): 
                            dollar += dictionary[word[i]]
                        if dollar == 100 and i == len(word)-1:
                            dollarStr = str(dollar)
                            writeFile.write(word+" = $"+dollarStr[0]+"."+dollarStr[1:]+'\n')

dict = {}  # @ReservedAssignment
dollarWords("list.txt","output.txt",prepareDictionary(dict))
