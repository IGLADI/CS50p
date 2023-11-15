def main():
    while True:
        try:
            fuelfraction = input("Fraction: ")
            fuel = convert(fuelfraction)
            if fuel <= 100:
                break
        except:
            pass
    print(gauge(fuel))


def convert(fraction):
    fractions = int(fraction.split("/")[0]), int(fraction.split("/")[1])
    return int(round((fractions[0] / fractions[1] * 100)))


def gauge(percentage):
    return "E" if percentage <= 1 else "F" if percentage >= 99 else f"{percentage}%"


if __name__ == "__main__":
    main()

