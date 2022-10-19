# Function to create a list with all possible permutations combinations
# For each element in LW, do a permutation with another element further in the loop
# there are 2 'cursors' i & j who do the permutation. For each i, j go further and try all the other elements.
#
#  ABCD => ABCD => BACD put in listPermut => ABCD => CBAD put in listPermut => ABCD => DBCA put in listPermut => ABCD => ABCD
#  ^    => ^^   =>                        => ^ ^  =>                        => ^  ^ =>                        =>  ^   =>  ^^  
def permutate(w:str):
    listPermut=[]
    
    i = 0
    for l in w:
        lw = list(w)
        j=i
        for z in lw[i:]:
            lw = list(w)
            lw[i], lw[j] = lw[j], lw[i]
            print(lw, "avec inversement de ", lw[i], "et", lw[j])
            lw1 = "".join(lw)
            listPermut.append(lw1)
            j+=1

        i+=1

    return listPermut

# Function to delete the duplicates
# -> for each element of the list, check if there is another one elsewhere in the list
def deleteDuplicates(l:list):
    i=0
    while i+1 <= len(l):             
        if l[i] in l[i+1:]:
            del l[i]
        i+=1
    return l

# Define the word entered by the user
word = str(input("Please enter a word or a string: "))
if type(word) is not str:
    word = str(input("You didn't enter a string\nPlease enter a word or a string: "))
word = word.lower()

# Find all combinations of permutations
result = permutate(word)
print("Step 1 :", result, "<-- List created")

# Remove all duplicata
result = deleteDuplicates(result)
print("Step 2 :", result, "<-- Duplicates deleted")

# Sorting of the list in alphabetical order
result.sort()
print("Step 3 :", result, "<-- List sorted")

# Find index of the word entered by user, variable 'word'
wordIndex = result.index(word)
print("Step 4 : index of", word.upper(), "is", wordIndex)

if wordIndex == len(result)-1:
    print(">> There is no result because all the possibilities are alphabetically before the word entered")
else:
    print(">> The first possibility alphabetically after the word entered is:", result[wordIndex+1].upper())
