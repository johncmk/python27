#!/usr/bin/python3
#HW0

#Generate dictionary
def prepareDictionary(dictionary):
    for key in range(97,123):
        dictionary[chr(key)] = (key-96)
    return dictionary

#ask user input words
def userInputWord(word):
    while(True):
        word = input("Enter words(after finishing input words enter 'f'):")
        if word == 'f' or word == 'F':
            break
        else:
            inputWords.append(word)
    return inputWords

#Write output.txt file if word costs a dollar
def dollarWordsCalculator(dollarWords,NotDollarWords,inputWords,dictionary):
    for line in inputWords:
        dollar,word = 0,line.lower().strip()
        if len(word) > 4: 
            for i in range(0,len(word)):
                if word[i].isdigit() or word[i] == ' ':
                    break
                if word[i] in dictionary.keys(): 
                    dollar += dictionary[word[i]]
                if dollar == 100 and i == len(word)-1:
                    dollarWords.append(word)
                elif dollar != 100 and i == len(word)-1:
                    NotDollarWords.append(word)

def printResult(dollarWords,NotDollarWords):    
    print("***dollar words***")
    for word in dollarWords:
        print(word)
    
    print("***Not a dollar words***")    
    for word in NotDollarWords:
        print(word)
    
dollarWords,NotDollarWords,inputWords,dict = [],[],[],{}  # @ReservedAssignment
dollarWordsCalculator(dollarWords,NotDollarWords,userInputWord(inputWords),prepareDictionary(dict))
printResult(dollarWords, NotDollarWords)

