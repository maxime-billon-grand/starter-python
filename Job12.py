f = open("./File_job12/data.txt", "r")

wordlist= f.read().split(" ")
#for word in wordlist:
    
#    if not word.isalpha():
#        i = wordlist.index(word)
#        del wordlist[i]

nbr = len(wordlist)

print("In the data.txt file, there are",nbr,"words")

