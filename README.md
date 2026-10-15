# Python Discount Calculator

A simple desktop application built with Python and Tkinter to calculate the final price of items after applying a discount.

This project was created as part of the Advanced Teacher Project for the IT Teacher recruitment process at Koding Next Indonesia.

## Features

- **Original Price Input** — Enter the original price of an item.
- **Discount Percentage** — Enter the discount rate as a percentage.
- **Quantity Input** — Specify the number of items.
- **Automatic Calculation** — Calculate the subtotal, discount amount, and final price.
- **Input Validation** — Handle invalid inputs and prevent negative prices, invalid discount rates, and non-positive quantities.
- **Clear Function** — Reset the input fields and calculation results.
- **Graphical User Interface** — Use a simple desktop interface built with Tkinter.

## Technologies Used

- Python 3
- Tkinter

## Requirements

- Python 3 installed on your computer.
- Tkinter, which is included with many Python installations.

On Ubuntu or Debian-based Linux distributions, install Tkinter if necessary:

```bash
sudo apt update
sudo apt install python3-tk
```

## How to Run

1. Clone this repository or download the project files.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python3 discount_calculator.py
```

4. Enter the original price, discount percentage, and quantity.
5. Click **Calculate** to display the calculation result.
6. Click **Clear** to reset the form.

## Calculation Formula

The application calculates the final price using the following formulas:

```python
subtotal = original_price * quantity
discount_amount = subtotal * discount_rate / 100
final_price = subtotal - discount_amount
```

### Example Calculation

Suppose the user enters:

| Input | Value |
|---|---:|
| Original Price | Rp 20,000 |
| Discount | 25% |
| Quantity | 3 |

The calculation is:

- Subtotal: Rp 20,000 × 3 = Rp 60,000
- Discount Amount: Rp 60,000 × 25% = Rp 15,000
- Final Price: Rp 60,000 − Rp 15,000 = Rp 45,000

**Expected Final Price: Rp 45,000.00**

## Learning Objectives

This project demonstrates fundamental programming concepts, including:

- Variables and data types
- User input and output
- Numeric type conversion
- Arithmetic operators
- Conditional statements
- Input validation
- Functions and event handling
- Basic graphical user interface development

## Project Structure

```text
python-discount-calculator/
├── discount_calculator.py
└── README.md
```

## Author

**All Arief Panca**

IT Teacher Candidate | Frontend Developer

- GitHub: https://github.com/allarief
- LinkedIn: https://www.linkedin.com/in/all-arief-panca-9a4b60214/

---

This project was developed for educational purposes to demonstrate basic Python programming and GUI development.