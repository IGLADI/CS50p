import sys
import csv


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        print("Files must be a csv file")
        sys.exit(1)
    else:
        first_names = []
        last_names = []
        houses = []
        with open(sys.argv[1], "r", encoding="utf-8") as input_csv_file:
            input_csv_file = csv.DictReader(input_csv_file)
            for row in input_csv_file:
                first_names.append(row["name"].split(", ")[1])
                last_names.append(row["name"].split(", ")[0])
                houses.append(row["house"])
        with open(sys.argv[2], "w", encoding="utf-8") as output_csv_file:
            fieldnames = ["first", "last", "house"]
            output_csv_file = csv.DictWriter(output_csv_file, fieldnames=fieldnames)
            output_csv_file.writeheader()
            for i, _ in enumerate(first_names):
                output_csv_file.writerow({"first": first_names[i], "last": last_names[i], "house": houses[i]})


if __name__ == "__main__":
    main()
