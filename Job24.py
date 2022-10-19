# This function do the calcul of the points of a word because of a dictionnary with the points of each letter
def points(word:str):
    dicoPoints={"a":1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 10, "l": 1, "m": 2, "n": 1, "o": 1, "p": 3, "q": 8, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 10, "x": 10, "y": 10, "z": 10}
    p=0
    for letter in word:
        p = p + dicoPoints[letter]
    
    return p

# This function will retrun true if the 2 strings are anagrams
def isAnagram(w1:str, w2:str):
    list2=list(w2)
    res = True
    for i in w1:
        if i in list2:
            list2.remove(i)
        else:
            res = False
    return res

# This function is for the sorting key  
def secondCriteria(tuple):
    return tuple[1]




# Asking for the word, and re-asking until he enter a valid value, then lowercase the string
word = str(input("Please enter a string : "))
while not word.isalpha():
    word = str(input("You didn't enter a valid string\nPlease enter a string : "))
word = word.lower()


# First loop to create a list with all word with same number of letters than the one entered by user
listAnagrams=[]
for item in open("./File_job24/dico_france.txt", "r"):
    if len(item)-1 == len(word):
        listAnagrams.append(item.rstrip())
if listAnagrams == []:
    print("There is no anagram with the same number of letter that you entered.")
    exit()

# Second loop to remove word that are not an anagram of the one entered by the user
for item2 in reversed(listAnagrams):
    if not isAnagram(word, item2):
        listAnagrams.remove(item2)
if listAnagrams == []:
    print("There is no anagram to the word you entered.")
    exit()

# Creation of a new list containing tuples (word, points)
listResults=[]

for a in listAnagrams:
    listResults.append((a, points(a)))

# Sorting of the list by points and in Descending order
listResults.sort(key=secondCriteria, reverse=True)

# Printing the results
for result in listResults:
    print("For", result[1], "points, you have the word :", result[0])



