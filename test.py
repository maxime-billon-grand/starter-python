wordlist = ["Hello", "world", "hey!", "comment", "va?"]
for word in wordlist:
    i = wordlist.index(word)
    if not word.isalpha():
        del wordlist[i]

print(wordlist)