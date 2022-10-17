f = open("./File_job12/data.txt", "r")

nbr = len(f.read().split(" "))

print("In the data.txt file, there are",nbr,"words")

