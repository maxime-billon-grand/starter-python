for i in range(1, 100):
    if i%5 == 0 and i%3 == 0:
        j = "FizzBuzz"
    elif i%3 == 0:
        j = "Fizz"
    elif i%5 == 0:
        j = "Buzz"
    else:
        j = i
    print(j)