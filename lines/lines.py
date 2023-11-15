import sys

def main():
    if (len(sys.argv) < 2):
        print("Too few command-line arguments")
        sys.exit(1)
    elif (len(sys.argv) > 2):
        print("Too many command-line arguments")
        sys.exit(1)
    elif not(sys.argv[1].endswith(".py")):
        print("File must be a Python file")
        sys.exit(1)
    else:
        lines = 0
        with open(sys.argv[1]) as python_file:
            for row in python_file:
                if str(row).strip() and not str(row).strip().startswith("#"):
                    lines += 1
        print(lines)

if __name__ == "__main__":
    main()