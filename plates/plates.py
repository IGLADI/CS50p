def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num = False
    if (2 <= len(s) <= 6) == False:
        return False
    if (s[0].isalpha() and s[1].isalpha()) == False:
        return False
    for letter in s:
        if letter in [".",",","!","?"," "] or num == True and letter.isalpha() == True or letter == "0" and num == False: 
            return False
        num = letter.isnumeric()
    return True

    
main()