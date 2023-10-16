while True:
    try:
        fuelfraction = input("Fraction: ")
        fractions = int(fuelfraction.split("/")[0]), int(fuelfraction.split("/")[1])
        if (fractions[0]<=fractions[1]):
            break
    except:
        pass
fuel = int(round((fractions[0]/fractions[1]*100)))
print("E") if fuel <= 1 else print("F") if fuel >= 99 else print(f"{fuel}%")
# inline if just for fun, old simple version: 
# if fuel <= 1:
#     print("E")
# elif fuel >= 99:
#     print("F")
# else:
#     print(f"{fuel}%")