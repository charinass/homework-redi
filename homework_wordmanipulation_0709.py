# Manipulating words
# edited for best practices
# make sure that every function only works as that,
# so that when it's called from another file
# it should not add additional processes but only as the function requires
# it is best to separate each function and call it from the main where the entire functions are required
# 2. edit to create into a class
# please contribute if you want, the goal is to be able to use best principles for flexibility
# naming convention needs improvement on this homework


class CounterOfStrings:

    def __init__(self, strInput):
        self.strInput = strInput.lower()

    def createArrayOfString(self):  # split each word into a list
        self.newString = self.strInput.split(sep=" ")
        return self.newString

    def countDistinctString(self):
        wordCount = {}
        # calling a function within a function inside a class requires 'self.'
        for word in (self.createArrayOfString()):
            if (word not in wordCount):  # append only if unique
                wordCount[word] = self.newString.count(word)
        wordCount = dict(sorted(wordCount.items()))
        return wordCount

    def mostFreqWord(self):
        mostFreqWords = []
        callDict = self.countDistinctString()
        maxCount = max(callDict.values())
        for key, value in callDict.items():
            if (value == maxCount):
                mostFreqWords.append(key)
        return mostFreqWords


strInput = input("Enter a sentence: \n").strip(" ")  # enter a string
# I want to be able to call each function even without calling them by order
displayInput = CounterOfStrings(strInput)
# putting comment on each function for trial & error if it works independently
# (my goal is to be able to use each function without depending on the others)
print(displayInput.countDistinctString())  # display dict of words
print(displayInput.createArrayOfString())  # display str as list
print(displayInput.mostFreqWord())  # display most frequent word
