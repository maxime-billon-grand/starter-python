
# 
#    |...../\               |....../\
#    |..../..\              |...../..\
#    |.../....\             |..../....\
#    |../......\            |.../......\
#    |./........\           |../........\
#    |/__________\          |./..........\         
#      height = 6           |/____________\
#                             height = 7
# 
# The number of spaces before the triangle is "size-1" at the top, and then do -1 at each line
# The number of spaces inside the triangle is 0 at the top and then do +2 at each line
# 
# 


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
# I tried to put only one big "print" function for each but it appear it add some additionnal spaces
