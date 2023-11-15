import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not (sys.argv[1].endswith(".csv")):
        print("File must be a csv file")
        sys.exit(1)
    else:
        table = []
        with open(sys.argv[1]) as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            for row in reader:
                table.append(row)
        print(tabulate(table,headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
