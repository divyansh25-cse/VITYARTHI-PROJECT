# storage.py

import os
from typing import Dict

BILLS_FILE = "bills_log.txt"


def save_bill(bill_text: str, bill_no: int, timestamp: str, total: float) -> None:
    """Append bill summary + full text to a log file."""
    with open(BILLS_FILE, "a", encoding="utf-8") as f:
        f.write(f"=== BILL {bill_no} | {timestamp} | Total: Rs.{total:.2f} ===\n")
        f.write(bill_text)
        f.write("\n\n")


def compute_summary() -> Dict[str, float]:
    """Very simple summary: count bills and total revenue from the log file."""
    if not os.path.exists(BILLS_FILE):
        return {"bill_count": 0, "total_revenue": 0.0}

    bill_count = 0
    total_revenue = 0.0

    with open(BILLS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("=== BILL"):
                bill_count += 1
                # line format: === BILL <no> | <timestamp> | Total: Rs.<amount> ===
                try:
                    part = line.split("Total: Rs.")[1]
                    amount_str = part.split()[0]
                    total_revenue += float(amount_str)
                except (IndexError, ValueError):
                    pass

    return {"bill_count": bill_count, "total_revenue": total_revenue}
