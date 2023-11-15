def main():
    hour = input("What time is it? ")
    hour = convert(hour)
    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")

def convert(time):
    temptime = time.split(":")
    return int(temptime[0]) + int(temptime[1])/60
    """This is a docstring"""
    """
    This is a multiline docstring
    This is a multiline docstring
    """
# do not
if __name__ == "__main__":
    main()