def handle_delivery(order_total):
    delivery = input("Do you want home delivery? (Yes/No): ")
    delivery_charge = 0
    address = ""
    phone = ""

    if delivery.lower() == "yes":
        address = input("Enter your delivery address: ")
        phone = input("Enter your phone number: ")
        if order_total >= 500:
            print("Free delivery unlocked!")
        else:
            delivery_charge = 40
            order_total += delivery_charge
        print(f"Your order will be delivered to: {address}")
        print(f"Phone: {phone}")
    else:
        print("You have selected takeaway.")

    print(f"The total amount to pay is Rs{order_total}")
    return order_total, address, phone, delivery_charge