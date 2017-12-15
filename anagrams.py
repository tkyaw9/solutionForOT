import sys


def main():
    allWords = readFile(sys.argv[1])
    userInput = raw_input(">")
    while userInput!="":
        result = ""
        for word in findWord(allWords, userInput):
            result += " " + word
        print result
        userInput = raw_input(">")

def findWord(allWords, word):
    cWord = compressWord(word)
    if cWord in allWords:
        return allWords[cWord]
    else:
        return "-"

def readFile(filename):
    f = open(filename)
    allWords = {}
    for line in f:
        word = line.strip()
        cWord = compressWord(word)
        if cWord not in allWords:
            allWords[cWord] = [word]
        else:
            binarySearchAndAdd(allWords, cWord, word)
    return allWords

def binarySearchAndAdd(allWords, cWord, word):
    l = allWords[cWord]

    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low + high)/2
        if l[mid] == word:
            return mid
        elif l[mid] < word:
            low = mid + 1
        elif l[mid] > word:
            high = mid - 1
    l.insert(low, word)
    allWords[cWord] = l

def compressWord(word):
    d = {}
    word = word.lower()
    for i in range(len(word)):
        if word[i] not in d:
            d[word[i]] = 1
        else:
            d[word[i]] += 1
    final = ""

    for k,v in sorted(d.items()):
        final += str(k)
        final += str(v)
    return final
main()
