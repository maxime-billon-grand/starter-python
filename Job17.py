def undefinedList(*nbr:int):
    for n in nbr:                                           # Check if all nbr are integer
        if type(n)is not int:
            raise TypeError (n + " is not an integer")

    myList=[]
    for i in nbr:
        if i%2 == 0:
            myList.append(i)

    return myList

print(undefinedList(2, 5, 4, 6, 7))
