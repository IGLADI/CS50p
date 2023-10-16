names = []
try:
    while True:
        name = input("Name: ")
        names += [name]
except EOFError:
    if (len(names)==2):
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        for i, name in enumerate(names):
            if i == 0:
                print(f"Adieu, adieu, to {name}")
            else:
                print(f"Adieu, adieu, to", end="")
                for j in range(i):
                    print(f" {names[j]}", end=",")
                print (f" and {name}")