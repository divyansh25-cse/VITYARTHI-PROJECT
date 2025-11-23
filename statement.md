Project Statement: Command-Line Café Ordering System

Problem Statement

The manual processing of orders in a café—involving note-taking, complex arithmetic, and price lookups—is inherently inefficient and error-prone. This project addresses the need for a simple, electronic, and deterministic system to automate the core transaction workflow. The solution must centralize the menu data, accurately record customer selections (including item accumulation), validate user input to ensure system stability, and instantly generate a clear, itemized bill.

Scope of the Project

The scope of the Command-Line Café Ordering System is intentionally narrow and focused on core transaction logic.

Included in Scope

Excluded from Scope

- Menu display and pricing (hardcoded)

- Graphical User Interface (GUI) or web interface

- Sequential order taking (single transaction)

- Database or file storage (no data persistence)

- Quantity validation (integer check)

- Inventory management or stock tracking

- Final bill calculation and display

- User authentication or multiple user roles

- Basic error handling (\texttt{ValueError})

- Discounts, taxes, or complex pricing rules

The project is limited to a single-session, in-memory application run via the terminal.

Target Users

The primary target users for this system are individuals who need a reliable, quick way to simulate or manage simple financial transactions in a service environment.

Primary User: Cashier / Service Staff: The individual directly interacting with the command-line interface to input customer orders and generate the bill.

Secondary User: Students / Developers: Individuals learning Python who can use the simple, procedural code as a foundational example of input handling, dictionary use, and transactional logic.

High-Level Features

The system offers the following key capabilities:

Interactive Menu Access: Users can immediately view all available items and prices upon startup.

Seamless Order Entry: The system remains open for continuous item entry until the transaction is manually closed using the designated command.

Robust Input Handling: The application gracefully manages incorrect data types (e.g., non-numeric quantity) without crashing, preserving system reliability.

Real-Time Accumulation: Quantities for repeated items are tracked and summed automatically.

Itemized Billing: A final, clearly formatted receipt is generated, showing item details, subtotals, and the grand total.
