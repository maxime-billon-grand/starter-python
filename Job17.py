def undefinedList(*nbr:int):
    l=[]
    for i in nbr:
        if i%2 == 0:
            l.append(i)

    return l

print(undefinedList(2, 3, 4, 6, 7))
