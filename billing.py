# billing.py

import datetime
import random
from typing import Dict
from menu import MENU, GST_RATE


def calculate_subtotal(order: Dict[str, int]) -> float:
    return sum(MENU[item] * qty for item, qty in order.items())


def calculate_gst(subtotal: float) -> float:
    return subtotal * GST_RATE


def calculate_total(subtotal: float, gst: float) -> float:
    return subtotal + gst


def generate_bill_number() -> int:
    return random.randint(10000, 99999)


def current_timestamp() -> str:
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def build_bill_text(order: Dict[str, int]) -> str:
    if not order:
        raise ValueError("No items in order")

    subtotal = calculate_subtotal(order)
    gst = calculate_gst(subtotal)
    total = calculate_total(subtotal, gst)
    bill_no = generate_bill_number()
    ts = current_timestamp()

    lines = []
    lines.append("--------- Cafe Bill ---------")
    lines.append(f"Bill No   : {bill_no}")
    lines.append(f"Date/Time : {ts}")
    lines.append("")
    lines.append("Items:")
    lines.append("-----------------------------")

    for item, qty in order.items():
        line_total = MENU[item] * qty
        lines.append(f"{item} x {qty} = Rs.{line_total}")

    lines.append("-----------------------------")
    lines.append(f"Subtotal : Rs.{subtotal:.2f}")
    lines.append(f"GST 18%  : Rs.{gst:.2f}")
    lines.append(f"TOTAL    : Rs.{total:.2f}")
    lines.append("-----------------------------")
    lines.append("Thank you! Visit again :)")

    return "\n".join(lines), bill_no, ts, total
