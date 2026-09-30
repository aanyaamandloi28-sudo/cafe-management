def handle_event_booking():
    print("\n========== EVENT BOOKING ==========")
    event = input("Do you want to book an event at Bistro? (Yes/No): ")
    
    event_charge = 0
    event_type = ""
    guests = 0
    
    if event.lower() == "yes":
        print("\nEvent Types:")
        print("1. Birthday - Rs2000 (Decoration + Cake)")
        print("2. Anniversary - Rs3000")
        print("3. Small Party / Meeting - Rs1500")
        
        event_type = input("Enter event type (Birthday/Anniversary/Party): ")
        guests = int(input("Enter number of guests: "))
        date = input("Enter event date (DD-MM-YYYY): ")
        
        if event_type.lower() == "birthday":
            event_charge = 2000
        elif event_type.lower() == "anniversary":
            event_charge = 3000
        elif event_type.lower() == "party":
            event_charge = 1500
        else:
            event_charge = 1500
            
        print(f"\nEvent '{event_type}' booked for {date}")
        print(f"Guests: {guests}")
        print(f"Event charge: Rs{event_charge}")
    else:
        print("No event booked.")
    
    return event_charge, event_type, guests