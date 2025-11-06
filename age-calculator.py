#age-calculator


from datetime import date, datetime

def validate_date_input(day, month, year):
    """Validate that the entered date is real and not in the future."""
    try:
        birth_date = date(year, month, day)
        if birth_date > date.today():
            print("❌ The birth date cannot be in the future.")
            return None
        return birth_date
    except ValueError:
        print("❌ Invalid date. Please enter a valid day, month, and year.")
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
    print("╔═══════════════════════════════════════════════╗")
    print("║           PYTHON AGE CALCULATOR               ║")
    print("╚═══════════════════════════════════════════════╝\n")

    while True:
        print("Please enter your birth date:")
        try:
            day = int(input("Day (1-31): "))
            month = int(input("Month (1-12): "))
            year = int(input("Year (e.g., 2000): "))
        except ValueError:
            print("❌ Please enter only valid numbers.\n")
            continue

        birth_date = validate_date_input(day, month, year)
        if not birth_date:
            continue

        years, months, days = calculate_age(birth_date)
        print(f"\n✅ You are {years} years, {months} months, and {days} days old.\n")

        again = input("Would you like to calculate another age? (y/n): ").lower()
        if again != "y":
            print("\n👋 Thanks for using the Age Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
