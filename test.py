s="hello world, test, test"
l=list(s)
print(l)
#s2 = " ".join(l)
#print(s2)






wordlist = ["Hello", "world", "hey!", "comment", "va?"]
for word in wordlist:
    i = wordlist.index(word)
    if not word.isalpha():
        del wordlist[i]

#print(wordlist)