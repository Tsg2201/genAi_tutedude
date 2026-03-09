# Python Functions Utility Assignment

## Overview

This project contains a collection of small Python utilities built to practice core function concepts.
The focus is on writing **simple, reusable functions** using Python fundamentals such as:

* User-defined functions
* Recursive functions
* Lambda functions
* `map()`
* `filter()`
* Default arguments

The tasks simulate basic operations that could appear in an **online billing or utility automation system**, such as applying discounts, calculating GST, and processing price lists.

---

## Project Structure

```
python-functions-assignment/

Task1.py
Task2.py
Task3.py
Task4.py
Task5.py
Task6.py
Task7.py
README.md
```

---

## Tasks

### Task 1 — Price After Discount

Implements a function that calculates the final price after applying a discount.

Features:

* Uses **default arguments**
* Ensures discount does not exceed **60%**
* Demonstrates simple function usage

---

### Task 2 — Recursive Factorial

Implements a **recursive function** to calculate factorial.

Features:

* Handles base cases (`0` and `1`)
* Prints an error for negative numbers
* Demonstrates recursion

---

### Task 3 — GST Calculator (Lambda)

Uses a **lambda function** to calculate price after adding **18% GST**.

Features:

* Simple lambda expression
* Optional lambda combining **GST + discount**

---

### Task 4 — Applying GST with `map()`

Applies the GST lambda to a list of prices using `map()`.

Features:

* Demonstrates list transformation using `map()`
* Generates a new list of prices after GST

---

### Task 5 — Filtering Expensive Products

Uses `filter()` to separate prices based on value.

Features:

* Filters prices **greater than 500**
* Filters prices **less than or equal to 500**

---

### Task 6 — Combined Price Processing

Creates a function that processes prices using both `map()` and `filter()`.

Steps:

1. Apply **10% discount** using `map()`
2. Filter prices **above 300**
3. Return both lists

---

### Task 7 — Menu Using Functions

Implements a small interactive program using functions.

Functions included:

* `add_price()` – adds price to list
* `get_average_price()` – returns average price
* `get_max_price()` – returns highest price

The program runs using a **simple menu system**.

---

## Requirements

* Python 3.x
* No external libraries required

Run any task using:

```
python Task1.py
```

---

## Key Learning Outcomes

* Writing **clean reusable functions**
* Understanding **recursion**
* Using **lambda expressions**
* Applying **map() and filter()**
* Structuring small Python programs clearly
