import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.match(
        r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
        ip,
    ):
        return False
    else:
        return True


if __name__ == "__main__":
    main()
