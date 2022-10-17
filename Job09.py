size = int(input("Please enter the height of the triangle: "))
if size == 0:
    print("Size is null.")
    exit()

s = 1
y, z = size - 1, 0

space = " "

while s <= size:

    if s == size:
        print(y*space, end="")
        print("/",end="")
        print(z*"_",end="")
        print("\\")
    else:
        print(y*space, end="")
        print("/",end="")
        print(z*space,end="")
        print("\\")
    s+=1
    y-=1
    z+=2
