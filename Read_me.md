# Expense Tracker 

## Description

Simple Python CLI project to track and categorize personal expenses using a dictionary.

## Features

- 3 categories:
  - F: Food
  - D: Divertissement
  - T: Taxes
- Counts total number of expenses
- Calculates:
  - Total per category
  - Global total
  - Percentage breakdown
- Displays a summary dashboard before exit

## How It Works

- User selects a category (F, D, T).
- User enters an expense amount (integer).
- Expense is stored in a dictionary list.
- When the user exits (Y), the program:
  - Calculates totals using `sum()`
  - Displays totals per category
  - Shows percentage distribution (if total > 0)

## Requirements

- Python 3.x
- No external libraries needed


