# test_billing.py

from billing import calculate_subtotal, calculate_gst, calculate_total
from menu import MENU, GST_RATE


def test_simple_bill():
    order = {"Coffee": 2, "Sandwich": 1}  # 2*50 + 1*70 = 170
    subtotal = calculate_subtotal(order)
    gst = calculate_gst(subtotal)
    total = calculate_total(subtotal, gst)

    assert subtotal == 170
    assert abs(gst - subtotal * GST_RATE) < 0.001
    assert abs(total - (subtotal + gst)) < 0.001

    print("All tests passed.")


if __name__ == "__main__":
    test_simple_bill()
