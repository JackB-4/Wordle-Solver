from calendar import c
import random
from collections import Counter
from wordlist import *
from english_words import english_words_lower_alpha_set

wordSize = input("How large is the word you are guessing?")
mainList = []
count = 0


def main():
    if wordSize != 5:
        wordChoice = "3"
    else:
        print("Choose which word bank to use.")
        print("1. Wordle Answer Bank")
        print("2. Wordle Full Bank")
        print("3. Large English Bank")
        wordChoice = input()

    if wordChoice == "1":
        for x in conciseWords:
            mainList.append(x)
    elif wordChoice == "2":
        for x in words:
            mainList.append(x)
    elif wordChoice == "3":
        for x in english_words_lower_alpha_set:
            if len(x) == int(wordSize):
                mainList.append(x)
    else:
        print("Choice is invalid.")
        main()
    #print(mainList)
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

def softlist(yellowInput, letterIndex, colorTrue):
    global mainList
    tempList = []
    
    for word in mainList:
        if yellowInput in word and colorTrue == True:
            tempList.append(word)
        elif colorTrue == False:
            tempList.append(word)
    mainList = tempList
    for item in mainList:
        if item[letterIndex] == yellowInput:
            mainList.remove(item)
    



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
    elif count == 0 and wordSize == "5":
        randomWord = "tares"
    else:
        print(mainList)
        randomWord = random.choice(mainList)
    
    count = 1




    print("Recommended Word: " + randomWord)
    fullWord = input("Type the last entered word with no punctuation.")
    fullWordList = [char for char in fullWord]
    #Dupe correction
    counts = Counter(fullWordList)
    dupes = [value for value, count in counts.items() if count > 1]
    # print(dupes)

    #Function triggering
    wordColors = input("Type the letter of the color of each letter with no spaces. (b,y,g)")
    wordColorList = [char for char in wordColors]

    cycle = 0
    for x in wordColorList:
        if x == "b" and fullWordList[cycle] not in dupes:
            blackList(fullWordList[cycle])
            # print("Post Blacklist: ", mainList)
        elif x == "y":
            softlist(fullWordList[cycle],cycle, True)
            # print("Post Softlist: ", mainList)
        elif x == "g":
            whiteList(fullWordList[cycle], cycle)
            # print("Post Whitelist: ", mainList)
        elif x == "b" and fullWordList[cycle] in dupes:
            softlist(fullWordList[cycle], cycle, False)
            # print("Post DupeList: ", mainList)
        else:
            print("Choice is invalid.")
            fullInput()
        cycle = cycle + 1
    print(mainList)
    fullInput()

main()