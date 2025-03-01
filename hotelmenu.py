#define the menu of restaurant
menu = {
    'pizza': 40,
    'burger' : 60,
    'sandwich' : 70,
    'salad' : 90,
    'drinks' : 60,
}

#greet
print("Welcome To Our Local Restuarant")
print("Here goes our menu.")
print("pizza: RS 40\nburger: RS 60\nsandwich: RS 70\nsalad: RS90\ndrinks: RS60")

order_total = 0
item1 = input("Enter the name of item you want to order:")

if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your order.")
else:
    print(f"Sorry!...Your item {item1} is currently unavailable.")
    
another_order = input("Do you want to add something more in your order? (Yes/No):")
if another_order == "yes":
    item2 = input("Enter the name of the another item you want to add:")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your item {item2} has been added in your order. ")
    else:
        print(f"Sorry!...Your item {item2} is currently unavailable.")

print(f"Your total amount to pay is {order_total}")
print("Thanks for choosing us.")  
    
    