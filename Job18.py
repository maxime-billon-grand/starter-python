def sortList(*nbr:int):

    for n in nbr:                                       # Check if all nbr are integer
        if type(n)is not int:
            raise TypeError (n + " is not an integer")

    myList=[]
    for i in nbr:
        myList.append(i)
    myList.sort()
    print(myList)
