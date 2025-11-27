📄 Project Statement — Cafe Billing System (CLI Based)
1. Project Title

•Cafe Billing System (CLI Application in Python)

2. Problem Statement

Small cafés often depend on manual billing, which leads to calculation mistakes, slower service, inconsistent record-keeping, and no automated daily reporting.
A simple, reliable, and efficient billing tool is required to automate the process of taking orders, calculating totals, applying GST, generating bills, and maintaining sales records.

The Cafe Billing System solves these problems by offering a Command Line Interface (CLI) based billing solution that is modular, easy to use, and ensures accurate calculations.

3. Purpose of the Project

•To provide a fast and accurate billing system for café operations

•To enable café staff to generate bills efficiently using a text-based CLI

•To automate GST calculation and total billing

•To maintain a persistent log of bills for record-keeping

•To generate daily sales summaries without manual effort

•To demonstrate modular Python programming and software engineering practices

4. Scope of the Project
Included in Scope

•Command Line Interface (CLI) based menu navigation

•Order entry and quantity management

•Subtotal, GST (18%), and total calculation

•Automatic bill generation with timestamp and unique bill number

•Saving each bill in a file (bills_log.txt)

•Summary report showing:

•Total bills generated

•Total revenue

•Modular implementation using multiple .py files

•Testing using a separate test script

Excluded from Scope

•Graphical User Interface (GUI)

•Online payment processing

•Database integration

•Inventory management

•Multi-user authentication system

5. Project Objectives

•Develop a CLI-based billing system using Python.

•Implement accurate billing computations including GST.

•Store bills persistently for future reference.

•Provide a summary of total sales and number of bills generated.

•Use a modular architecture consisting of 5+ Python files.

•Demonstrate file handling, testing, and structural clarity as required by the academic rubric.

6. Functional Requirements

•Display Menu

•System should show a list of available items and their prices.

•Order Management

•Add items with quantity

•View current order

•Clear entire order

•Billing Functionality

•Calculate subtotal

•Apply GST of 18%

•Calculate final total

•Generate unique bill number

•Generate timestamp

•Print formatted bill

•Bill Storage

•Save bill data to bills_log.txt

•Sales Summary

•Show total number of bills

•Show total revenue collected

•Exit System

•User can exit the program through CLI menu

7. Non-Functional Requirements

•Usability

The CLI interface must be simple, clear, and user-friendly.

•Reliability

System should generate correct billing amounts consistently.

•Maintainability

Code should be modular with logical separation across multiple Python files.

•Performance

Computations must run instantly without noticeable delay.

•Portability

Program must run on any system with Python installed (Windows, macOS, Linux).

•Data Integrity

Bills must be saved correctly and not overwritten.

8. Constraints

•Program must run in Python 3.x

•Only standard Python libraries to be used

•CLI-only interface (no GUI used)

•Local file-based storage (no database)

9. Assumptions

•User has basic understanding of operating a CLI

•Café menu items and prices remain constant

•Bill log file is accessible and writable

•Python interpreter is installed on the user’s system

10. Methodology

•Used a modular design approach with files:

•main.py – CLI controller

•menu.py – Menu data

•billing.py – Billing logic

•storage.py – File storage + summary

•test_billing.py – Validations

•Designed system architecture before coding

•Verified functions through test cases

•Implemented error handling and input validation

11. Expected Outcome

A fully functional, reliable, and easy-to-use CLI-powered cafe billing system capable of handling end-to-end billing operations, storing sales data, and generating summaries — all while being modular and well-documented.

12. Conclusion

The Cafe Billing System successfully meets the objectives of automating café billing using a clean and efficient Command Line Interface (CLI).
Its modular structure, billing accuracy, file storage, and reporting capabilities fulfill all academic requirements and demonstrate a solid understanding of Python programming and software engineering best practices.
