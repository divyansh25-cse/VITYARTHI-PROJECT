# main.py

from typing import Dict
from menu import MENU
from billing import build_bill_text
from storage import save_bill, compute_summary


def show_menu():
    print("\n--- CAFE MENU ---")
    for item, price in MENU.items():
        print(f"{item:10s} : Rs.{price}")
    print("-----------------\n")


def show_order(order: Dict[str, int]):
    if not order:
        print("Current order is empty.")
        return
    print("\n--- CURRENT ORDER ---")
    for item, qty in order.items():
        print(f"{item:10s} x {qty}")
    print("---------------------\n")


def add_item_to_order(order: Dict[str, int]):
    show_menu()
    item = input("Enter item name: ").strip()
    if item not in MENU:
        print("Invalid item. Please choose from the menu.")
        return

    qty_str = input("Enter quantity: ").strip()
    if not qty_str.isdigit() or int(qty_str) <= 0:
        print("Quantity must be a positive integer.")
        return

    qty = int(qty_str)
    order[item] = order.get(item, 0) + qty
    print(f"Added {item} x {qty} to order.")


def generate_and_save_bill(order: Dict[str, int]):
    if not order:
        print("No items in order. Add items first.")
        return

    try:
        bill_text, bill_no, ts, total = build_bill_text(order)
    except ValueError as e:
        print("Error:", e)
        return

    print("\n" + bill_text + "\n")

    save_bill(bill_text, bill_no, ts, total)
    print("Bill saved to file.")
    order.clear()


def show_summary_menu():
    summary = compute_summary()
    print("\n--- SALES SUMMARY (from log file) ---")
    print(f"Total bills   : {summary['bill_count']}")
    print(f"Total revenue : Rs.{summary['total_revenue']:.2f}")
    print("-------------------------------------\n")


def main():
    order: Dict[str, int] = {}

    while True:
        print("==== CAFE BILLING SYSTEM ====")
        print("1. Show menu")
        print("2. Add item to order")
        print("3. View current order")
        print("4. Generate bill")
        print("5. Show sales summary")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_item_to_order(order)
        elif choice == "3":
            show_order(order)
        elif choice == "4":
            generate_and_save_bill(order)
        elif choice == "5":
            show_summary_menu()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
