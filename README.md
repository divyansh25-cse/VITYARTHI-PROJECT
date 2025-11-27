📘 Cafe Billing System – Python (CLI Project)

A fully modular Command Line Interface (CLI) based billing system built in Python.
This project automates café billing, GST calculation, order management, and sales reporting.
It follows all academic requirements: modularity, architecture, testing, and documentation.

⭐ 1. Project Overview

The Café Billing System is a Python-based CLI application that allows staff to take orders, compute totals with GST, generate formatted bills, and store them for reporting.

This project uses a multi-file modular structure, demonstrating clean separation of logic, file handling, testing, and proper software engineering practices.

🎯 2. Objectives

•Provide a simple CLI-based user interface.

•Automate subtotal, GST (18%), and total calculation.

•Generate bills with timestamps and unique bill numbers.

•Save every bill in a log file.

•Produce daily sales summaries.

•Demonstrate modular programming in Python.

✨ 3. Features
✔ Command Line Interface (CLI)

•Fast and interactive

•No GUI required

•Perfect for academic modular projects

✔ Order Management

•Add items with quantity

•View current order

•Clear order

•Input validation

✔ Billing

•Subtotal calculation

•Auto GST (18%)

•Final total

•Timestamp + bill number

•Printable bill format

✔ Storage & Reporting

•Saves all bills to bills_log.txt

•Summary report includes:

•Total bills

•Total revenue

✔ Modular Design (Full Marks Requirement)

•main.py – CLI + program flow

•menu.py – Menu prices

•billing.py – GST + billing logic

•storage.py – File handling + reporting

•test_billing.py – Testing logic

🗂 4. Project Structure
CafeBillingProject/
│
├── main.py
├── menu.py
├── billing.py
├── storage.py
├── test_billing.py
│
├── README.md
└── bills_log.txt   ← Auto-created

🏗 5. System Architecture
+-------------------------+
|     User (CLI Input)    |
+-------------+-----------+
              |
              v
+-------------+-----------+
|           main.py       |
| (CLI + Program Control) |
+------+------+-----------+
       |      |
       |      |
       v      v
+------+---+  +------------------+
| menu.py |  |   billing.py      |
| (Prices)|  | (All calculations)|
+----+----+  +--------+----------+
               |
               v
        +------+-------------+
        |     storage.py     |
        | (Save + Summary)   |
        +---------------------+

🧪 6. Testing

test_billing.py verifies:

•Subtotal calculation

•GST computation

•Total calculation logic

•Run tests:
python test_billing.py

▶️ 7. How to Run (CLI)
•Step 1 — Clone repo
git clone https://github.com/<your-username>/<your-repo>.git

•Step 2 — Enter project folder
cd CafeBillingProject

•Step 3 — Run program
python main.py

📦 8. Bill Storage

Bills are stored in:

bills_log.txt


Each bill includes:

•Bill number

•Timestamp

•Items & quantities

•Subtotal

•GST

•Total

This file is used for generating daily summaries.

🚀 9. Future Enhancements

•GUI version (Tkinter)

•Discount coupons

•Payment options

•Export PDF bills

•Database integration (SQLite)

👤 10. Author

•Divyansh Agarwal
