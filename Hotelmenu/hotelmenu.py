#DEfine the menu of restaurant
menu = {
    'pizza': 100,
    'burger': 90,
    'coffee': 45,
    'salad': 70,
    'pasta': 85, 
}

#Greet
print("Welcome to python restaurant")
print("pizza: rs40/nPasta: rs90/nBurger: rs70/nSalad rs45/nCoffee: ")

order_total = 0
#80+ 70 = 150

item_1 =input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 +50
    print(f"ypur item {item_1} has been added to your order")
    
else:
    print(f"ordered item {item_1} is npt available yet!")
    
    item_1 = input ("enter the name of item you want to order=")
    
another_order = input("do youwant to add another item ? (yes/no) ") 
if another_order == "yes":
    item_2 = input("enter the name of second  item = ")     
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2}is not available!")
print (f"the total amount of items to pay is {order_total}")                 