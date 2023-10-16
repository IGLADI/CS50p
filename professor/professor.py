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
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
        else:
            raise ValueError("Invalid level")

if __name__ == "__main__":
    main()