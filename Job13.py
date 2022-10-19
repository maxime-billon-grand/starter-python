# Asking for the word size to look for
size = int(input("Please enter a word size: "))

# Opening the file
f = open("./File_job12/data.txt", "r")

# Create a list of string with all words
wordlist = f.read().split(" ")

# Creating a dictionnary with the {size : number of words with this size}
larousse = {}

for i in wordlist:
    if i.isalpha():
        j = len(i)
        larousse[j] = larousse.get(j, 0) +1

# dico[size] will be the number of words with size letters
print("There are",larousse[size],"word with",size,"letters")
print(larousse)
