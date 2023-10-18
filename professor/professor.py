import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        problemx = generate_integer(level)
        problemy = generate_integer(level)
        for trys in range(3):
            print(f"{problemx} + {problemy} = ", end="")
            answer = int(input(""))
            if answer == problemx + problemy:
                score += 1
                break
            else:
                print("EEE")
                if trys == 2:
                    print(f"{problemx} + {problemy} = {problemx + problemy}")
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and 1 <= int(level) <= 3:
            return int(level)
        else:
            print("Invalid input.")


def generate_integer(level):
    for _ in range(10):
        if level in [1, 2, 3]:
            return random.randint(10 ** ((level - 1)) if level != 1 else 0, int("9" * level))
        else:
            raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
