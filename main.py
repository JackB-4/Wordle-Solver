import random
from wordlist import *
from english_words import english_words_lower_alpha_set

mainList = []
count = 0


def main():
    print("Choose which word bank to use.")
    print("1. Wordle Answer Bank")
    print("2. Wordle Full Bank")
    print("3. Large English Bank")
    wordChoice = input()
    if wordChoice == "1":
        for x in conciseWords:
            if len(x) == 5:
                mainList.append(x)
    elif wordChoice == "2":
        for x in words:
            if len(x) == 5:
                mainList.append(x)
    elif wordChoice == "3":
        for x in english_words_lower_alpha_set:
            if len(x) == 5:
                mainList.append(x)
    else:
        print("Choice is invalid.")
        main()

    fullInput()


def whiteList(whitelistInput, whitelistPositionInput):
    global mainList
    tempList = []

    for word in mainList:
        if word[whitelistPositionInput] == whitelistInput:
            tempList.append(word)
    mainList = tempList
    

def blackList(blacklistInput):
    global mainList
    tempList = []

    for word in mainList:
        for char in word:
            if char == blacklistInput:
                tempList.append(word)

    for item in tempList:
        if item in mainList:
            mainList.remove(item)
    tempList = []

def softlist(yellowInput, letterIndex):
    global mainList
    yellowHistory = []

    yellowInput = list(yellowInput)
    for letter in yellowInput:
        if letter not in yellowHistory:
            yellowHistory.append(letter)
    
    mainList = [ele for ele in mainList if all(ch in ele for ch in yellowInput)]
    for word in mainList:
        if word[letterIndex] == yellowInput[0]:
            mainList.remove(word)
    



def fullInput():
    global mainList
    global count
    
    if count != 0:
        optimizedChoices = []
        for word in mainList:
            if "r" in word or "s" in word or "t" in word:
                optimizedChoices.append(word)
        if optimizedChoices:
            randomWord = random.choice(optimizedChoices)
        elif mainList:
            randomWord = random.choice(mainList)
        else:
            print("Word not found in database.")
            quit()
        optimizedChoices.clear()
    else:
        randomWord = "tares"
    
    count = 1




    print("Recommended Word: " + randomWord)
    fullWord = input("Type the last entered word with no punctuation.")
    fullWordList = [char for char in fullWord]

    wordColors = input("Type the letter of the color of each letter with no spaces. (b,y,g)")
    wordColorList = [char for char in wordColors]

    cycle = 0
    for x in wordColorList:
        if x == "b":
            blackList(fullWordList[cycle])
            print(mainList)
        elif x == "y":
            softlist(fullWordList[cycle],cycle)
            print(mainList)
        elif x == "g":
            whiteList(fullWordList[cycle], cycle)
            print(mainList)
        else:
            print("Choice is invalid.")
            fullInput()
        cycle = cycle + 1
    print(mainList)
    fullInput()

main()