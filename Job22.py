# This function create a substitute to the string.index() method
def searchLetterInList(letter:str, list:list):
    i,j = 0,0
    for l in list:
        if l == letter:
            j=i
            i+=1  
        i+=1
    return j


# Since we can't use any of the system function upper(), lower(), capitalize() or string.replace() or string.index(),
# these functions will use only the base functions

#==============Function UPPER======================
def myUpper(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    l = list(s)                         # Place str in a list
    j=0
    for letter in l:
        if letter in lower:
            i = searchLetterInList(letter, lower)
            l[j] = upper[i]
        j+=1
    s = "".join(l)                      # Recreate the str from the list
    return s

#==============Function LOWER======================
def myLower(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    l = list(s)                         # Place str in a list
    j=0
    for letter in s:
        if letter in upper:
            i=searchLetterInList(letter, upper)
            l[j] = lower[i]
        j+=1
    s = "".join(l)                      # Recreate the str from the list
    return s

#==============Function TITLE======================
def myTitle(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    l = list(s)                 # Place str in a list
# Replace the first character & the first character after space by the uppercase
    i = 0
    while i+1 <= len(l):
        if i == 0 or l[i-1] == " " and l[i] in lower:
            j=searchLetterInList(l[i], lower)
            l[i] = upper[j]

        i+=1

    s = "".join(l)              # Recreate the str from the list
    return s

#==============Function CLEAN======================
def myClean(s:str):
   
    l = list(s)                                 # Place str in a list 
    i = 0
    while i < len(l):

        if i == 0 and l[i] == " ":              # Delete spaces if there are any at the beginning
            del l[i]

        elif i+1 == len(l) and l[i] == " ":     # Delete space if there are any at the end
            del l[i]

        elif l[i] == " " and l[i+1] == " ":     # Delete space if there are 2 consecutives spaces
            del l[i]

        else:
            i+=1
    
    s = "".join(l)
    return s


# == For testing the functions ==
#print(myUpper("AbCdDyH1"))
#print(myLower("AbCdDyH1"))
#print(myTitle("hello world, test, test"))
#print(myClean("  hello  world  "))

chain = str(input("Please enter a string: "))
param = str(input("Please enter the parameter: upper / lower / title / clean: "))

match param:
    case "upper":
        print(myUpper(chain))
    case "lower":
        print(myLower(chain))
    case "title":
        print(myTitle(chain))
    case "clean":
        print(myClean(chain))
    case _:
        print("You didn't enter a valid parameter.")
