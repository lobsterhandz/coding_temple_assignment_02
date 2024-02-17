# ussr inputs a year
year = int(input("Enter a year: "))

# Check if year is leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Check if the year is a century
if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")

