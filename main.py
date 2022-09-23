# Created by Marcus chau
print("\033[4mhello\033[0m") # Underlined word


closeDictionary = {}

# main control that calls all the other functions
def fixer(word,dictionary):
    if word.lower() in dictionary:
        return word.lower()
    Tempword = ""
    tw = word[0].upper()
    Tempword += tw
    tw = word[1:]
    Tempword += tw
    if Tempword in dictionary:
        return Tempword
    removerWord = remover(word, dictionary)
    if word != removerWord:
        return removerWord
    adderWord = adder(word, dictionary)
    if word != adderWord:
        return adderWord
    closeWord = closeToFixer(word, dictionary)
    if word != closeWord:
        return closeWord
    return word


# function to remove a letter to check to see if that fixes the spelling error
def remover(word, dictionary):
    listOfLetters = []
    for letter in word:
        listOfLetters.append(letter)
    i = 0
    while len(word) > i:
        tempChar = listOfLetters[i]
        listOfLetters.remove(listOfLetters[i])
        tempString = ""
        for element in listOfLetters:
            tempString += element
        if tempString in dictionary:
            return tempString
        listOfLetters.insert(i, tempChar)
        i += 1
    return word


# function that checks the words around to see if that fixes the problem
def closeToFixer(word, dictionary):
    accm = 0
    while len(word) > accm:
        returnChar = closeDictionary[word[accm]]
        for i in returnChar:
            Word = word[0:accm] + i + word[accm + 1:]
            if Word in dictionary:
                return Word
        accm += 1
    return word


# Adds a letter to check to see if it fixes the spelling issue
def adder(word, dictionary):
    adderacc = 0
    while len(word) + 1 > adderacc:
        for i in range(97, 123):
            addTempString = word[0:adderacc] + chr(i) + word[adderacc:]
            if addTempString in dictionary:
                return addTempString
        adderacc += 1
    return word


# main method 
def main():
    lFile = open("keyboard-letters.txt")
    dfile = open("american-english.txt")
    dictionary = []
    for line in dfile:
        line = line.strip()
        dictionary.append(line)
    for line in lFile:
        key = line[0]
        restOfChar = line[2:]
        restOfChar = restOfChar.split()
        closeDictionary[key] = restOfChar
    userInput = input("Enter anything: ")
    words = userInput.split()
    end = ""
    for word in words:
        if not word in dictionary:
            finishedWord = fixer(word, dictionary)
            if word != finishedWord:
                end += f"\033[4m{finishedWord}\033[0m"
            else:
                end += word
        else:
            end += word
        end += " "
    print(end)


# calling main
main()
