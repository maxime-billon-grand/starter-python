# This program delete words which are attached to a special character
# Example: "vincitur," will be removed and not counted because of the coma.

# Since we try to do it with only the base function and no import, this code works but is a little long to execute and can use a lot of ressources.
# I'm sorry for the inconvenience


# To test the program, you can execute it with a smaller file, File-job12/data-test.txt
askTest = str(input("Do you want to test the program with a smaller file ? (Y/N)"))
match askTest:
    case "Y":
        f = open("./File_job12/data-test.txt", "r")
        wordlist= f.read().split(" ")
    case "N":
        f = open("./File_job12/data-test.txt", "r")
        wordlist= f.read().split(" ")
    case _:
        askTest = str(input("You didnt' enter a valid answer\nDo you want to test the program with a smaller file ? (Y/N):"))

i=0
while i+1 <= len(wordlist):
    if not wordlist[i].isalpha():
        del wordlist[i]
    i+=1
nbr = len(wordlist)

# You can uncomment this to see the list of the word and check it
#print(wordlist)

print("In the file, there are",nbr,"words without special caracteres")

