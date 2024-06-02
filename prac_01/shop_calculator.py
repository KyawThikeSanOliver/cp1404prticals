number_of_items = int(input("Number of items:"))
total_price = 0

while number_of_items <= 0:
    print("Invalid Items")
    num_of_items = int(input("Number of items:"))

for i in range(number_of_items):
    item_price = float(input("Price of item:"))
    total_price += item_price
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")
