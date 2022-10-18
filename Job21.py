def mySort(l:list):
    i=0
    while i+1 < len(l):

# Find minimum value in the last part of the list
        minimumValue = min(l[i: len(l)])

# Find the indice of the minimum value, remove it from the list and add it at the beginning of the list
        indexMin = l.index(minimumValue)
        del l[indexMin]
        l.insert(i, minimumValue)

        i+=1

    return l

def myDisplay(l:list):
    print(l)


