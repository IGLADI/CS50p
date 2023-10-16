formula = input("Expression: ")
values = formula.split(" ")
match values[1]:
    case "*":
        print(f"{float(values[0]) * float(values[2]):.1f}")
    case "/":
        print(f"{float(values[0]) / float(values[2]):.1f}")
    case "+":
        print(f"{float(values[0]) + float(values[2]):.1f}")
    case "-":
        print(f"{float(values[0]) - float(values[2]):.1f}")
