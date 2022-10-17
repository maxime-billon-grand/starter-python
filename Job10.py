
program=int(input("What do you want to do ?\n1 - Write in the file\n2 - Read in the file\n"))

# First part of the job
if program == 1:
    text = str(input("Please write your text: "))

    f = open("./Files_job10/output.txt", "a")
    f.write(text)
    f.close()

# Second part of the job
elif program == 2:
    f = open("./Files_job10/output.txt", "r")
    print(f.read())
    f.close()

else:
    print("You didn't enter the right option !")

# Script de Maxime Billon-Grand