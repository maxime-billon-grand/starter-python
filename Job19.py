# ================ Function with some of system function (len, min, insert) ====================================
def noSortList(*nbr:int):

    # Check if all nbr are integer
    for n in nbr:                                       
        if type(n)is not int:
            raise TypeError (n + " is not an integer")

    # Put the nbr in a list, they are in an tuple
    myList= list(nbr)

    # This is a loop which take the minimum value, move it at the beginning of the list
    # and then repeat the process in the list minus the element just moved. 
    i=0
    while i+1 < len(myList):

        # Find minimum value in the last part of the list
        minimumValue = min(myList[i: len(myList)])

        # Find the indice of the minimum value, remove it from the list and add it at the beginning of the list
        indexMin = myList.index(minimumValue)
        del myList[indexMin]
        myList.insert(i, minimumValue)

        i+=1

    print("The sorted list is:", myList)

# ================ Function with none of system function ================================================
def noSortList2(*nbr:int):
    
    for n in nbr:                                       # Check if all nbr are integer
        if type(n)is not int:
            raise TypeError (n + " is not an integer")

    l1 = list(nbr)                                      # Create 2 lists: L1 will be the origin, L1 will be the new sorted list
    l2 = list(nbr)

    i=0                                                 # Create i for the index of values of L1
    while l1:                                           # First loop, while there is any elements in L1
        mini = l1[0]                                    # Minimum value found in the remaining elements in L1

        k, j = 0, 0                                     # K is a value which will increment in the first loop, J will be used for store the index of the minimum value when found

        for e in l1:                                    # Second loop, look for the minimum value in the remaining elements in L1
            if e < mini:                                # When found an element smaller than mini,mini = element of remaining L1, and j will be 
                mini = e                                #   mini = element of remaining L1 and 
                j=k                                     #   and j will be the index of mini
            k+=1
        
        l2[i]=mini                                      # Replace the i element with the minimum value found in L2
        del l1[j]                                       # Delete the j element of L1

        i+=1


    print("The sorted list is:", l2)

    


noSortList(8, 10, 3, 5, 2, 7, 6)
noSortList2(3,2,8,9,5)
# Copyright Maxime Billon-Grand