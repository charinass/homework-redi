# Manipulating words
# edited for best practices
# make sure that every function only works as that,
# so that when it's called from another file
# it should not add additional processes but only as the function requires
# it is best to separate each function and call it from the main where the entire functions are required

def main():
    newInput = input("Enter a sentence: \n").strip(" ")  # enter a string
    strInput = newInput.lower()  # lowercase all letters
    newString = createArrayOfString(strInput)
    wordCount = countDistinctString(newString)
    mostFreqWord(wordCount)


def createArrayOfString(strInput):  # split each word into a list
    newString = strInput.split(sep=" ")
    print(newString, '\n')
    return newString


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
    return wordCount


def mostFreqWord(wordCount):
    maxCount = max(wordCount.values())
    for key, value in wordCount.items():  # print max when maxCount is satisfied
        if (value == maxCount):
            print(key)


if __name__ == "__main__":
    main()
