#Define the menu of cafe
#Drinks menu
drinks = {
      'Cold coffee':80,
      'Iced latte':80,
      'Hot chocolate':60,
      'Milkshake':100,
      'Green tea':60,
      'Masala tea':40,    
}
#Light_bites menu
light_bites = {
      'Omelette':100,
      'Croissant':180,
      'Muffin':180,
      'Avocado toast':200,
      'Garlic toast':220,
}
#Desserts menu
desserts = {
       'Chocolava cake':50,
       'Cheesecake':150,
       'Chocolate brownies':100,
       'Slice cake':120,
}
menu = {**drinks,**light_bites,**desserts}

#Greet
print("welcome to Bistro cafe!")
print("here is our menu:")

#Show drinks
print("Cold coffee: Rs80\nIced latte: Rs80\nHot chocolate: Rs60\nMilkshake: Rs100\nGreen tea: Rs60\nMasala tea: Rs40")

#Show light_bites
print("Omelette: Rs100\nCroissant: Rs180\nMuffin: Rs180\nAvocado toast: Rs200\nGarlic toast: Rs220")

#Show desserts
print("Chocolava cake: Rs50\nCheesecake: Rs150\nChocolate brownies: Rs100\nSlice cake: Rs120")

order_total=0
#40+220+60+150+120+50+200=840

while True:
    item = input("Enter the name of the item you want to order = ")
    if item in menu:
        order_total += menu[item] #0 + 40
        print(f"Your item {item} has been added to your order.")
        print(f"Current_total= Rs{order_total}")
    else:
        print(f"Ordered item {item} is not available yet!")
    another_order = input("Do you want to add another item? (Yes/No)")
    if another_order == "No":
        break

print(f"The total amount of item to pay is {order_total}")