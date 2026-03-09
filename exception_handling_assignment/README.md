# Python Exception Handling Assignment

This project contains solutions for **Assignment 6: Exception Handling**.

The goal is to practice Python exception handling using:

- try
- except
- multiple except blocks
- else
- finally
- raising custom exceptions

No classes or advanced modules were used as per assignment restrictions.

---

## File Structure

---

## Task Descriptions

### Task 1 — Safe Division Utility
- Takes numerator and denominator from the user.
- Handles:
  - `ValueError`
  - `ZeroDivisionError`
- Uses `else` and `finally`.

---

### Task 2 — Bill Calculator
- Iterates through a list of product prices.
- Skips invalid values.
- Raises custom exception for negative prices.
- Prints running total.

---

### Task 3 — Age Validator
- Uses a function `check_age(age)`.
- Raises a custom `ValueError` if age is outside **1–120**.
- Uses try-except to handle errors.

---

### Task 4 — File Reader
- Asks user for filename.
- Reads first **3 lines of the file**.
- Handles:
  - `FileNotFoundError`
  - `PermissionError`
- Uses `finally`.

---

### Task 5 — Safe Shopping Cart
- Accepts product prices from user input.
- Stops when user enters **'q'**.
- Handles:
  - invalid numeric input
  - negative price
- Displays:
  - total items
  - total bill

---

## How to Run

Example:
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
