def noSortList(*nbr:int):
    myList=[]
    for x in nbr:
        myList.append(x)

# This is a loop which take the minimum value, move it at the beginning of the list
# and then repeat the process in the list minus the element just moved. 
    i=0
    while i+1 < len(myList):

# Find minimum value in the last part of the list
        minimumValue = min(myList[i: len(myList)])
        print("The minimum of the list",myList[i: len(myList)], "is", minimumValue)

# Find the indice of the minimum value, remove it from the list and add it at the beginning of the list
        indexMin = myList.index(minimumValue)
        del myList[indexMin]
        myList.insert(i, minimumValue)

        i+=1

    print("The sorted list is:", myList)

noSortList(8, 10, 3, 5, 2, 7, 6)

# Copyright Maxime Billon-Grand