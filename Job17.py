def undefinedList(*nbr:int):
    myList=[]
    for i in nbr:
        if i%2 == 0:
            myList.append(i)

    print(myList)

undefinedList(2, 3, 4, 6, 7)
