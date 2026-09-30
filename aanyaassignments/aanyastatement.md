#BISTRO CAFE - Python Project Statement

Bistro Cafe Management System

Problem Statement

Managing cafe orders manually can result in incorrect calculations, difficulty in maintaining order details, and inefficient handling of delivery and other customer services.

The Bistro Cafe Management System is developed to provide a simple Python-based solution for managing cafe menu items, customer orders, billing, delivery, reservations, and event bookings.

Scope of the Project

The project focuses on developing a basic cafe management system using Python. It allows users to view menu items, select multiple food and beverage items, calculate the order total, choose delivery, enter delivery details, and manage additional cafe services such as reservations and event bookings.

The project is intended as an academic implementation of programming concepts and is not designed as a complete commercial cafe management platform.

Target Users

- Cafe staff
- Cafe managers
- Customers using the ordering system
- Students learning Python programming and software development concepts

High-Level Features

- Menu management
- Food and beverage selection
- Multiple-item ordering
- Quantity selection
- Automatic bill calculation
- Delivery option
- Delivery address and phone number collection
- Delivery charge calculation
- Table reservation
- Event booking
- Input validation and error handling
- Clear display of order and billing information

Technologies Used

- Python
- Python dictionaries and lists
- Conditional statements
- Loops
- Functions
- Input/output operations
- Exception/input validation where applicable

Expected Outcome

The system should provide a simple and organized way to demonstrate cafe ordering and management operations while applying Python programming concepts in a real-world context.

#1. Project Title
*Bistro Cafe Management System (Food Ordering + Seat Reservation + Event Booking + Home Delivery)*

#2. Objective
To create a simple console-based Python application for a cafe that handles food ordering, table reservation, event booking and delivery with final bill generation. This project is made for learning dictionary, loops, if-else, functions and modules.

#3. Project Files
File	Work
`cafemanagement.py`	Main file - shows menu, takes order, calls all modules, prints bill
`reservation.py`	Seat Reservation - 2, 4, 6 seater & Private cabin
`event.py`	Event Booking - Birthday Rs2000, Anniversary Rs3000, Party Rs1500
`delivery.py`	Home Delivery - Address, Phone, Free delivery above Rs500

#4. Features
*A. Food Ordering (ordering.py):*
Dictionary `menu` stores items. Loop takes orders and calculates `order_total`.

*B. Seat Reservation (reservation.py):*
Function `handle_seat_reservation()` asks for table booking. Charges: 2 & 4 seater Free, 6 seater Rs200, Private Rs500.

*C. Event Booking (event.py):*
Function `handle_event_booking()` books events with date and guests.

*D. Delivery (delivery.py):*
Function `handle_delivery(order_total)` - If total >= 500 free delivery else Rs40 charge.
*E. Final Bill:*
Prints Food + Reservation + Event + Delivery = TOTAL

5. Execution Flow
`START -> Show Menu -> Food Order -> Seat Reservation -> Event Booking -> Delivery -> Final Bill -> END`

6. Concepts Used
Dictionary, while loop, if-else, functions, return, module import, user input.

7. Sample Bill
Cold coffee - Rs80
Seat (4-Seater Table for 4 at 7:30 PM) - Rs0
Event (Birthday) - Rs2000
Delivery - Rs0
TOTAL TO PAY: Rs2080

8. Conclusion
This project combines 4 real-life cafe services into one Python program. It is modular and can be expanded with GST, payment method and GUI.