# solutionForOT

1. Offline runtime
My readFile function opens the file, and the reads every single line in the
given dictionary. For each word, I check whether I've seen a compressed version
of the word before. If it's not, I make a new list with the current word as value.
If it's not, I make a new entry. If we've already seen a compressed version of
the word though, we need to just append it to the list. 


Design Choice:

However, if we just
append it to the list, we eventually have to sort it later so that we can return
the words in lexicographical order. Therefore, I believe it's better if we add
it in a way that maintains the sorted order of the lists at all times.
This is where the binarySearchAndAdd function comes in. I'm not actually searching
for the word, because I know the word isn't in the list (since all words are unique);
however, I'm looking for where I should put it so the list remains sorted. This is
O(nlogn) (n is the length of the list in the dictionary) for each word in the dictionary.

This payoff is something we need to discuss if we're going to implement in real life.
On one hand, we can just append everything to the list, which is O(1), and then sort the
entire list every time the user gives a new input OR we could maintain the sorted list, but
we would have to do this O(nlogn) add every time we're adding a new word into the dictionary.
We could choose this approach (commented out in the code) if we know the data for the dictionary is preprocessed one time. 
In other words, the other approach would be great if we want to take less time preprocessing the data in the offline process
so in a way that ensures that the online process goes smoothly and efficiently.

However, in this case, since we know we'll be having about a million words in the dictionary, 
we'll just append to the list. So it'll take O(1) to just append to the list. However, when we 
call sorted on the list that FindWords return, it'll take O(nlogn) (n is the size of the list) for 
every word the user asks for, but we know that this will be limited by 10,000. 

In general, reading the file will take O(N) if N represents how many lines
there are in the dictionary, and for each word, (if we choose the binary search approach) 
it'll take O(nlogn) to add to a list in the dictionary.

Online runtime:

In main:
There's a while loop that goes on until the user enters nothing.
But within the while loop, there's a for-loop that loops over the list to
concatenate it into a string, and that takes O(lengthOfListinDictionary) and we
can upperbound that with the length of the longest list in the dictionary aka
the length of the largest group of anagrams.

But from within the for-loop, I actually call findWord, which just checks if
the compressed version of the word is in the dictionary, which is constant time.

The runtime of compressWord is O(lengthOfWordGiven), because it loops through
each letter and updates its frequency counter. To return the compressed version
of the word, I call sorted on the items in the dictionary and then concatenate
the letter and its count together. The sorting will take O(nlogn)
(n is the size of the dictionary) assuming Python's sorted function uses some sort of
smart sorting function (I think it's TimSort and
it's a mix and match of merge sort and something else). I could've used a
binary search and add but I figured the size of the dictionary is, in the worst case, 26
and it'll rarely be 26 unless a word has all 26 characters of the alphabet.

Overall, we call findWord, which calls compressWord which is
 O(length of word) + O(nlogn) to sort. From Main, we call findWord for each
 word that the user enters, and loop through the list findWord returns, which
 is O(lengthOfLongestListinDictionary).

2. Memory complexity:
The allWords dictionary will group the words by the anagrams they belong to.
In general, the size of the dictionary will be proportional to the number of
words there are since the sum of all the items in all the lists in the dictionary
should add up to the total number of given words in the original dictionary.

Every time we call compressWord, we create a mini-dictionary to keep track
of the frequency of the letters. This will be as big as the number of unique letters
in the word.
