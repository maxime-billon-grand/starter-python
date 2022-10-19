def permutate(w:str):
    listPermut=[]

    i = 0
    for l in w:
        lw = list(w)
        j=i
        for z in lw[i:]:
            lw = list(w)
            lw[i], lw[j] = lw[j], lw[i]
            print(lw, "avec inversement de ", lw[i], "et", lw[j])
            lw1 = "".join(lw)
            listPermut.append(lw1)
            j+=1

        i+=1

    return listPermut

def deleteDuplicates(l:list):
    i=0
    while i+1 <= len(l):
        if l[i] in l[i+1:]:
            del l[i]
        i+=1
    return l

r=permutate("love")
print(r)
r=deleteDuplicates(r)
print(r)

r.sort()
print(r)