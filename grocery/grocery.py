grocerys = {}
while True:
    try:
        item = input("")
        if item in grocerys:
            grocerys[item] += 1
        else:
            grocerys[item] = 1
    except EOFError:
        break
for item in sorted(grocerys):
    print(f"{grocerys[item]} {item.upper()}")