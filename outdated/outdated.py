monthlist = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    baddate = input("Date: ")
    try:
        date = baddate.split("/")
        day = date[1]
        month = date[0]
        year = date[2]
        if int(month)>12:
            raise Exception("Month is greater than 12")
        if int(day)>31:
            raise Exception("Day is greater than 31")
        break
    except:
        try:
            # can use if instead of try & raise 
            if "," not in baddate:
                raise Exception("No comma in date")
            date = baddate.replace(",","").split(" ")
            day = date[1]
            # or use index of monthlist instead of for loop
            for months in monthlist:
                if months.lower() == date[0].lower():
                    month = monthlist.index(months)+1
                    break
            if int(month)>12:
                raise Exception("Month is greater than 12")
            if int(day)>31:
                raise Exception("Day is greater than 31")
            year = date[2]
            break
        except:
            pass
if int(month)<10:
    month = f"0{month}"
if int(day)<10:
    day = f"0{day}"
print(f"{year}-{month}-{day}".replace(" ",""))