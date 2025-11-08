# age-calculator
🧮 Simple Python Age Calculator built with the datetime module. Calculates a person’s exact age from their birthdate using logical programming, date handling, and user-friendly interaction for real-world applications.

🎯 MAIN OBJECTIVE

Calculate the user's exact age based on a given birth date.

🧩 SECONDARY OBJECTIVES

Validate the user’s input step by step (day, month, year).

Prevent invalid values such as negative numbers or impossible calendar dates.

Allow the user to modify the day, month, or year before calculating the final age.

Maintain clean, readable logic and friendly command-line interaction.

🧠 LOGICAL FLOW (Commented Version)

# START
#   │
#   ▼
# Display introduction and explanation of the program
#   │
#   ▼
# Ask the user to enter:
# • Day (1–31)
# • Month (1–12)
# • Year (> 0)
#   │
#   ▼
# Validate the full date (must exist and cannot be in the future)
#   │
#   ▼
# Ask the user if they want to modify day, month, or year
#   ├──► If yes, revalidate the updated date
#   └──► If no, continue
#   │
#   ▼
# Calculate the age in years, months, and days
#   │
#   ▼
# Display the result
#   │
#   ▼
# Ask if the user wants to calculate another age
#   └──► If no, exit the program

📅 DATE RULES USED BY THE PROGRAM

The date is validated in two steps:

✅ 1. Individual validation

| Field | Rules |
|:------:|:-----|
| Day | Must be between 1 and 31 |
| Month | Must be between 1 and 12|
| Year | Must be positive |

✅ 2. Full date validation

After all three values are entered, the program checks:

The date exists (ex: Feb 30 is rejected)

The date is not in the future

🛠️ BUILT WITH

Python 3

Focus on logical programming and CLI interaction

Modular structure for easy readability and maintenance
