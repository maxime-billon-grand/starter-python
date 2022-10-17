def myAddition(v1, v2):
    if (type(v1) is not int and not float) or (type(v2) is not int and not float):
        return "You didn't enter numbers"

    return v1 + v2


result=myAddition(3.5, 9)
