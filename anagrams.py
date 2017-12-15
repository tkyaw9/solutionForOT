import sys

def main():
    allWords = readFile(sys.argv[1])
    #allWords is the dictionary of all the words
    userInput = raw_input(">")
    while userInput!="": 
        result = ""
        for word in sorted(findWord(allWords, userInput)):
            result += " " + word
        print result
        userInput = raw_input(">")

def findWord(allWords, word):
    cWord = compressWord(word) #all words are grouped by compression of anagrams
    if cWord in allWords:
        return allWords[cWord] #return list of words that are in this group of anagrams
    else:
        return "-"

def readFile(filename):
    #reads the file and returns a dictionary of 
    #{compressedAnagramString:[all words that are anagrams of each other]}
    f = open(filename)
    allWords = {}
    for line in f:
        word = line.strip() #get rid of white spaces and new line characters 
        cWord = compressWord(word) 
        if cWord not in allWords:
            allWords[cWord] = [word] #first time seeing the word
        else:
            allWords[cWord].append(word) #add to the right group of anagrams
            # binarySearchAndAdd(allWords, cWord, word)
    return allWords

def binarySearchAndAdd(allWords, cWord, word):
    #this is the optional binarySearchAndAdd function I was talking about in the README
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
    #binarySearch is a fast way (O(nlogn)) of manually maintaining the sortedness of a list as we add items to it;
    #this is an alternative option if we don't want to sort later
    allWords[cWord] = l

def compressWord(word):
    d = {}
    word = word.lower()
    #takes care of lower/upper case letter differences
    for i in range(len(word)):
        if word[i] not in d:
            d[word[i]] = 1
        else:
            d[word[i]] += 1 #updates counts/frequencies of the letters in the word
        
    final = ""
    for k,v in sorted(d.items()):
        #creates the compressed string for anagrams
        final += str(k)
        final += str(v)
    return final
main()
