# Manipulating words
def main():
    newInput = input("Enter a sentence: \n")  # enter a string
    if (newInput.count(' ') > 0):
        strInput = newInput.lower()  # lowercase all letters
        createArrayOfString(strInput)


def createArrayOfString(strInput):  # split each word into a list
    newString = strInput.split(sep=" ")
    print(newString, '\n')
    countDistinctString(newString)


def countDistinctString(newString):
    wordCount = {}
    uniqueWord = []
    for word in newString:
        if (word not in uniqueWord):  # append only if unique
            uniqueWord.append(word)

    uniqueWord.sort()  # to alphabetically sort the words
    for i in uniqueWord:
        print(i, ":", newString.count(i))
        wordCount[i] = newString.count(i)  # store in dictionary

    mostFreqWord(wordCount)


def mostFreqWord(wordCount):
    maxCount = max(wordCount.values())
    for key, value in wordCount.items():  # print max when maxCount is satisfied
        if (value == maxCount):
            print(key)


if __name__ == "__main__":
    main()
