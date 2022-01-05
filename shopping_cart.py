items = []
prices = []
action = ''

print("Welcome to the Shopping Cart Program!")

while action != "5":

    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("Please enter an action: ")

    if action == "1":
        new_item = input("What item would you like to add? ")
        items.append(new_item)
        new_item_price = float(input(f"What is the price of '{new_item}'? "))
        prices.append(new_item_price)
        print(f"'{new_item.capitalize()}' has been added to the cart.")

    elif action == '2':
        print("The contents of the shopping cart are:")
        for i in range(len(items)) and range(len(prices)):
            normal_item = items[i]
            normal_price = prices[i]
            index = i
            position = i + 1
            print(f"{position}. {normal_item} - ${normal_price:.2f}")

    elif action == '3':
        removed_item = int(input("Which item would you like to remove? "))
        removed_item_position = removed_item - 1
        last_position = len(items) - 1
        while removed_item_position < 0 or removed_item_position > last_position:
            print("Sorry, this item is not in the list. Try again.")
            removed_item = int(input("Which item would you like to remove? "))
            removed_item_position = removed_item - 1
        else:
            items.pop(removed_item_position)
            prices.pop(removed_item_position)
            print("Item removed")

    elif action == '4':
        for i in range(len(prices)):
            total_amount = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total_amount:.2f}")

    elif action == '5':
        print("Thank you. Goodbye.\n")

    else:
        print("This is not a valid action. Please enter a valid action.\n")