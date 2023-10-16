import random

def main():
    level = get_int("Level: ")
    random_number = random.randint(1, level)
    while True:
        guess = get_int("Guess: ")
        if guess == random_number:
            print("Just right!")
            break
        elif guess < random_number:
            print("Too small!")
        else:
            print("Too large!")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                pass
            else:
                return value
        except ValueError:
            pass
        
if __name__ == "__main__":
    main()