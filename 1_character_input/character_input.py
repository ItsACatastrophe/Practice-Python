from datetime import date, timedelta
from math import floor

# Constant representing day to year constant multiplier.
# Accounts for leap years. Not perfect but it'll do.
# Source: https://pumas.nasa.gov/examples/how-many-days-are-year
DATES_PER_YEAR = 365.2422


def main():
    print("this is a print from my main function")
    name: str = input("What is your name: ")
    age: str = input("And what is your age: ")

    years_until_old: int = 100 - int(age)

    # Date when user is 100. Could also just add 9 or 10 to old_date.year.
    old_date: date = date.today() + timedelta(
        days=floor(years_until_old * DATES_PER_YEAR)
    )

    print(
        f"Congratulations {name}, you will be 100 years old in either {old_date.year} or {old_date.year - 1}"
    )


if __name__ == "__main__":
    main()
