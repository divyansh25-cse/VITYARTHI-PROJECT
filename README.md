☕ Simple Command-Line Café Ordering System

Project Overview

This is a basic command-line application built in Python designed to simulate the core transactional process of a small café or restaurant. The system allows a cashier (or user) to view a fixed menu, take multiple orders sequentially, and instantly generate a final, itemized bill. The project emphasizes fundamental programming concepts like dictionary management, input validation, and simple arithmetic logic.

Features

The Café Ordering System provides the following core functionalities:

Menu Display: Displays all available food and drink items along with their respective prices (FR1).

Order Input: Allows continuous input of item names and quantities until the order is finalized (FR2, FR6).

Order Accumulation: Automatically adds ordered quantities if the same item is entered multiple times (FR5).

Input Validation: Handles non-numeric input for quantity and prompts the user for a correct integer value (FR4, NFR2).

Billing: Calculates the subtotal for each item and generates the final grand total for the order (FR7, NFR1).

Technologies/Tools Used

Language: Python 3.x

Data Structures: Python Dictionaries (for Menu and Order tracking)

Architecture: Command Line Interface (CLI)

Steps to Install & Run the Project

Since this is a single, self-contained Python script, installation is straightforward.

Prerequisites: Ensure you have Python 3.x installed on your system.

Save the Code: Save the provided Python code into a file named cafe_system.py.

Run the Script: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script using the Python interpreter:

python cafe_system.py


Interact: The program will prompt you to enter items from the menu until you type done.

Instructions for Testing

Manual Black Box testing was used to verify all functional and non-functional requirements.

Positive Test Cases (Success Scenarios)

Test Goal

Expected Input

Expected Outcome

Single Item Order

Coffee, quantity 1, then done

Total amount: Rs. 50

Accumulation

Tea, quantity 1, then Tea, quantity 2, then done

Tea quantity is 3, Total amount: Rs. 90

Mixed Order

Sandwich, quantity 1, Cake, quantity 1, then done

Total amount: Rs. 115

Negative Test Cases (Error Scenarios)

Test Goal

Input

Expected Outcome

Invalid Item

Item: Soda

System prints "Item not found in menu." and prompts again.

Invalid Quantity

Item: Juice, Quantity: ten

System prints "Please enter a valid number for quantity." and prompts for quantity again.

Case Sensitivity (Current Limitation)

Item: coffee

System prints "Item not found in menu." (Identified limitation).
