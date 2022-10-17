lenght = int(input("Please enter the lenght : "))
height = int(input("Please enter the height : "))
if lenght == 0 or height == 0:
    print("Lenght or height is null.")
    exit()
l, h = 1, 1
tiret = "-"
space = " "

while h <= height:
    print("|", end="")
    if h == 1 or h == height:
        print((lenght-2)*tiret, end="")
    else:
        print((lenght-2)*space, end="")
    print("|")
    h +=1
