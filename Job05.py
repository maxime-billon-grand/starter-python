val1 = int(input("Valeur 1 : "))
val2 = int(input("Valeur 2 : "))

if val1 == val2:
    print("Les deux valeurs sont égales")
elif val1 < val2:
    for i in range(val1, val2):
        print(i)
else:
    for i in range(val1, val2, -1):
        print(i)


