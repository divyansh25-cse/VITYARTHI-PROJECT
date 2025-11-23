menu = {
    "Coffee": 50,
    "Tea": 30,
    "Sandwich": 70,
    "Cake": 45,
    "Juice": 40
}

print("Welcome to the Cafe!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

order = {}
while True:
    choice = input("Enter item to order (or 'done' to finish): ").strip()
    if choice.lower() == "done":
        break
    if choice not in menu:
        print("Item not found in menu.")
        continue
    quantity = input(f"Enter quantity for {choice}: ")
    try:
        quantity = int(quantity)
        if choice in order:
            order[choice] += quantity
        else:
            order[choice] = quantity
    except ValueError:
        print("Please enter a valid number for quantity.")

total = sum(menu[item] * qty for item, qty in order.items())

print("\n----- Bill -----")
for item, qty in order.items():
    print(f"{item} x {qty}: Rs.{menu[item]*qty}")
print(f"Total amount: Rs.{total}")

print("Thank you for visiting!")
