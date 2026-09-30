#Bistro Cafe Management System

A simple console-based Python project for managing a cafe - including Food Ordering, Seat Reservation, Event Booking, and Home Delivery.

###Project Files

File Description
| `bistro.py` / `Cafe management.py` | Main file - Shows menu, takes order, prints final bill |
| `reservation.py` | Seat Reservation module |
| `event.py` | Event Booking module |
| `delivery.py` | Home Delivery module |
| `statement.md` | Project documentation |
| `README.md` | This file |

###Features

**1. Food Ordering**
- Menu stored in Dictionary
- Users can order multiple items
- Auto-calculates total

**2. Seat Reservation**
- 2-Seater: Free
- 4-Seater: Free
- 6-Seater Family: Rs. 200
- Private Cabin (8 Persons): Rs. 500

**3. Event Booking**
- Birthday: Rs. 2000
- Anniversary: Rs. 3000
- Small Party: Rs. 1500

**4. Delivery**
- Free delivery on orders >= Rs. 500
- Otherwise Rs. 40 charge
- Takes Address and Phone

**5. Final Bill**
`Food + Reservation + Event + Delivery = TOTAL`

###How to Run

1. Keep all 4 `.py` files in SAME folder
2. Open `bistro.py` in Pydroid 3
3. Press PLAY button
4. Follow the instructions on screen

**Flow:**
`Show Menu -> Food Order -> Seat Reservation -> Event Booking -> Delivery -> Final Bill`

### Concepts Used
- Python Dictionary
- While Loop & If-Else
- Functions & Return values
- Module Import (`from ... import ...`)
- User Input/Output

### Testing section:
TC01
·Valid menu item
·Item added to order
TC02
·Valid quantity
·Correct quantity added
TC03
·Multiple items
·All items included in order
TC04
·Delivery = Yes
·Address and phone requested
TC05
·Delivery = Yes
·₹40 delivery charge added
TC06
·Delivery = No
·No delivery charge
TC07
·Invalid menu choice
·Error/validation message
TC08
·Order completed
·Correct final total displayed

### Sample Bill
Cold coffee - Rs80
Seat (4-Seater Table for 4 at 7:30 PM) - Rs0
Event (Birthday) - Rs2000
Delivery - Rs0
TOTAL TO PAY: Rs2080
Thank you for choosing Bistro Cafe!

### Future Improvements
- GST & Payment Method (UPI/Cash)
- Save bill to text file
- GUI version using Tkinter