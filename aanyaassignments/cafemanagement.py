from delivery import handle_delivery
from event import handle_event_booking
from reservation import handle_seat_reservation

menu = {
    "Cold coffee": 80, "Iced latte": 80, "Hot chocolate": 60,
    "Milkshake": 100, "Green tea": 60, "Masala tea": 40,
    "Omelette": 100, "Croissant": 180, "Muffin": 180,
    "Avocado toast": 200, "Garlic toast": 220,
    "Chocolava cake": 50, "Cheesecake": 150,
    "Chocolate brownies": 100, "Slice cake": 120
}

print("welcome to Bistro cafe!")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0
ordered_items = []
    
while True:
    item = input("\nEnter item name = ")
    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"Added {item}. Total= Rs{order_total}")
    else:
        print("Not in menu")
    if input("Add more? (Yes/No) ").lower() == "no":
        break
 
# 1. Seat Reservation
res_charge, table_no, persons, res_time = handle_seat_reservation()
order_total += res_charge

# 2. Event Booking
event_charge, event_type, guests = handle_event_booking()
order_total += event_charge

# 3. Delivery
order_total, address, phone, delivery_charge = handle_delivery(order_total)

# FINAL BILL
print("\n== FINAL BILL ==")
for i in ordered_items:
    print(f"{i} - Rs{menu[i]}")
print(f"Seat Reservation ({table_no}): Rs{res_charge}")
print(f"Event Charge ({event_type}): Rs{event_charge}")
print(f"Delivery: Rs{delivery_charge}")
print(f"TOTAL TO PAY: Rs{order_total}")
print("Thank you for choosing Bistro Cafe!")