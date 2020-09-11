# Manipulating words
# edited for best practices
# make sure that every function only works as that,
# so that when it's called from another file
# it should not add additional processes but only as the function requires
# it is best to separate each function and call it from the main where the entire functions are required
# 2. edit to create into a class
# please contribute if you want, I want to make this better


class CounterOfStrings:

    def __init__(self, strInput):
        self.strInput = strInput

    def createArrayOfString(self):  # split each word into a list
        self.newString = self.strInput.split(sep=" ")
        return self.newString

    def countDistinctString(self):
        self.wordCount = {}
        # calling a function within a function inside a class requires 'self.'
        for word in (self.createArrayOfString()):
            if (word not in self.wordCount):  # append only if unique
                self.wordCount[word] = self.newString.count(word)
        wordCount = dict(sorted(self.wordCount.items()))
        return wordCount

    def mostFreqWord(self):
        mostFreqWords = []
        callDict = self.countDistinctString()
        maxCount = max(callDict, key=callDict.get)
        for key, value in callDict.items():
            if (value == callDict[maxCount]):
                mostFreqWords.append(key)
        return mostFreqWords


newInput = input("Enter a sentence: \n").strip(" ")  # enter a string
strInput = newInput.lower()  # lowercase all letters
# I want to be able to call each function even without calling them by order
displayInput = CounterOfStrings(strInput)
# print(displayInput.createArrayOfString()) #just a trial (my goal is to be able to use each function without depending on the others)
# print(displayInput.countDistinctString())
print(displayInput.mostFreqWord())
