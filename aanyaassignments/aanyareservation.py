def handle_seat_reservation():
    print("\n========== SEAT RESERVATION ==========")
    reservation_charge = 0
    table_no = "No Reservation"
    persons = 0
    time = ""

    reserve = input("Do you want to reserve a table? (Yes/No): ")

    if reserve.lower() == "yes":
        print("\nTable Options:")
        print("1. 2-Seater - Free")
        print("2. 4-Seater - Free")
        print("3. 6-Seater Family - Rs200")
        print("4. Private Cabin (8 persons) - Rs500")

        persons = input("Enter number of persons: ")
        table_type = input("Enter table type (2/4/6/Private): ")
        time = input("Enter reservation time (e.g. 7:30 PM): ")
        name = input("Enter the name of the customer: ")

        if table_type == "6":
            reservation_charge = 200
            table_no = "6-Seater Family Table"
        elif table_type.lower() == "private":
            reservation_charge = 500
            table_no = "Private Cabin"
        elif table_type == "4":
            table_no = "4-Seater Table"
        else:
            table_no = "2-Seater Table"

        print(f"\nTable {table_no} reserved for {persons} persons at {time}")
        if reservation_charge > 0:
            print(f"Reservation Charge: Rs{reservation_charge}")
        else:
            print("No extra charge for reservation!")
    else:
        print("No table reservation.")

    return reservation_charge, table_no, persons, time