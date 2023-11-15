import validators


def is_valid_email(email):
    return validators.email(email)


def main():
    user_email = input("Please enter an email address: ")
    if is_valid_email(user_email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
