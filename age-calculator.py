#age-calculator


from datetime import date, datetime

#validate date in parts
def get_valid_day():
    while True:
        try:
            day = int(input("Day (1–31): "))
            if 1 <= day <= 31:
                return day
            else:
                print("❌ Day must be between 1 and 31.")
        except ValueError:
            print("❌ Please enter a valid number.")


def get_valid_month():
    while True:
        try:
            month = int(input("Month (1–12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("❌ Month must be between 1 and 12.")
        except ValueError:
            print("❌ Please enter a valid number.")


def get_valid_year():
    while True:
        try:
            year = int(input("Year (e.g., 2000): "))
            if year > 0:
                return year
            else:
                print("❌ Year must be positive.")
        except ValueError:
            print("❌ Please enter a valid number.")
def validate_full_date(day, month, year):
    from datetime import date

    try:
        birth_date = date(year, month, day)

        if birth_date > date.today():
            print("❌ The birth date cannot be in the future.")
            return None

        return birth_date

    except ValueError:
        print("❌ The date does not exist. Please enter it again.\n")
        return None


def calculate_age(birth_date):
    """Calculate age in years, months, and days."""
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust for negative values
    if days < 0:
        months -= 1
        last_month = (today.month - 1) or 12
        last_year = today.year if today.month != 1 else today.year - 1
        days += (date(last_year, last_month + 1, 1) - date(last_year, last_month, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def main():
    print(
    "Welcome to the Python Age Calculator! 👋\n"
    "This program lets you calculate your exact age in:\n"
    "   • Years\n"
    "   • Months\n"
    "   • Days\n"
    "\nJust enter your birth date and the calculator will do the rest.\n")

    print("With this program you can:")
    print(" - Enter your birth date easily")
    print(" - Automatically validate the date")
    print(" - Get your exact age with precision")
    print(" - Repeat the calculation as many times as you want\n")

    while True:
        print("Please enter your birth date:")

        day = get_valid_day()
        month = get_valid_month()
        year = get_valid_year()

        birth_date = validate_full_date(day, month, year)
        if birth_date:
            break

        years, months, days = calculate_age(birth_date)
        print(f"\n✅ You are {years} years, {months} months, and {days} days old.\n")

        again = input("Would you like to calculate another age? (y/n): ").lower()
        if again != "y":
            print("\n👋 Thanks for using the Age Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
