from datetime import date
import sys
import datetime
import inflect


def get_user_input():
    user_input = input("Date of Birth: ")
    year, month, day = user_input.split("-")
    return year, month, day

def to_words(before):
    p = inflect.engine()
    after = p.number_to_words(before)
    after = after[0].upper() + after[1:]
    after = after.replace("and ", "")
    after += " minutes"
    return after

def main():
    try:
        year, month, day = get_user_input()
    except ValueError:
        sys.exit("Invalid date format")
    user_dob = datetime.date(int(year), int(month), int(day))
    today = date.today()
    age_in_minutes = (today - user_dob).total_seconds() / 60
    age_in_minutes = to_words(int(age_in_minutes))
    print(age_in_minutes)


if __name__ == "__main__":
    main()
