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


    return l2


print(noSortList2(3,2,8,9,5))


