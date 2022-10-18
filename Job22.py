def myUpper(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for l in s:
        if l in lower:
            i=lower.index(l)
            s=s.replace(l, upper[i])
    return s

def myLower(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for l in s:
        if l in upper:
            i=upper.index(l)
            s=s.replace(l, lower[i])
    return s

def myTitle(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Place str in a list
    l = list(s)

# Replace the first character and the first character after space by the uppercase
    i = 0
    while i+1 <= len(l):
        if i == 0 or l[i-1] == " " and l[i] in lower:
            j=lower.index(l[i])
            l[i] = upper[j]

        i+=1

# Recreate the str from the list
    s = "".join(l)
    
    return s


def myClean(s:str):
    l = list(s)
    i = 0
    tour = 1
    while i < len(l):
        print("tour :", tour,"- i=", i, " :", l, len(l))
        if i == 0 and l[i] == " ":
            del l[i]
            print("manip1")

        elif i+1 == len(l) and l[i] == " ":
            del l[i]
            print("manip2")

        elif l[i] == " " and l[i+1] == " ":
            del l[i]
            print("manip3")

        else:
            i+=1
        
        print("tour :", tour,"- i=", i, " :", l, len(l))
        tour +=1
    
    s = "".join(l)
    print(l)
    return s

#chain = str(input("Please enter a string: "))
#param = str(input("Please enter the parameter: upper / lower / title / clean"))


print(myUpper("AbCdDyH1"))
print(myLower("AbCdDyH"))
print(myTitle("hello world, test, test"))
print(myClean("  hello  world  "))