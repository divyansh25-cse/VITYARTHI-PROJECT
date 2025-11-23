Cafe Billing System (Python)
A simple console-based cafe billing system written in basic Python.
It allows the user to select items from a menu, enter quantities, and then displays a detailed bill with the total amount.

Features
Displays a fixed menu with item names and prices.

Lets the user enter item names and quantities in a loop.

Validates menu items and handles invalid inputs.

Calculates and shows per-item cost and total bill amount.

Requirements
Python 3.x installed on your system.

No external libraries are required (only built-in Python functions).

How to Run
Save the Python code in a file, for example: cafe_billing.py.

Open a terminal or command prompt in the folder containing the file.

Run the program with:

bash
python cafe_billing.py
Follow the on-screen instructions:

Type the item name exactly as shown in the menu.

Enter the quantity as an integer.

Type done when you have finished ordering.

Code Overview
A dictionary menu stores item names as keys and prices as values.

A dictionary order stores ordered items and their total quantities.

A loop takes user input until done is entered.

At the end, the program multiplies price × quantity for each item and prints a formatted bill with the final total.

Possible Improvements
Add GST/tax and discount calculations.

Save bills to a file for record-keeping.

Add input validation for negative or zero quantities.

Convert the program into a GUI app using Tkinter or a web app using Flask/Django.
