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

        for word in self.newString:
            if (word not in self.wordCount):  # append only if unique
                self.wordCount[word] = self.newString.count(word)

        return sorted(self.wordCount.items())

    def mostFreqWord(self):
        mostFreqWords = []
        maxCount = max(self.wordCount.values())
        for key, value in self.wordCount.items():  # print max when maxCount is satisfied
            if (value == maxCount):
                mostFreqWords.append(key)
        return mostFreqWords


newInput = input("Enter a sentence: \n").strip(" ")  # enter a string
strInput = newInput.lower()  # lowercase all letters
displayInput = CounterOfStrings(strInput)
print(displayInput.createArrayOfString())
print(displayInput.countDistinctString())
print(displayInput.mostFreqWord())
