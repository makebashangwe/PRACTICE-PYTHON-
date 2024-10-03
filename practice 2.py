import sys

class Store:
    def __init__(self, inventory):
        self.store_inventory = inventory
        self.user_cart = {}  # Changed to a dictionary to store items and quantities

    def add(self, item, quantity):
        if item in self.store_inventory:
            if self.store_inventory[item]['stock_quantity'] >= quantity:
                self.user_cart[item] = self.user_cart.get(item, 0) + quantity
                self.store_inventory[item]['stock_quantity'] -= quantity
                print(f"Added {quantity} {item}(s) to your cart.")
            else:
                print("Not enough stock.")
        else:
            print("Item not found.")

    def display_store_inventory(self):
        print("Store Inventory:")
        for item, details in self.store_inventory.items():
            print(f"{item}: {details['stock_quantity']} in stock at ${details['individual_price']} each.")

    def display_user_cart(self):
        if not self.user_cart:
            print("Your cart is empty...")
            return

        subtotal = 0
        print("Your cart: ")
        for item, quantity in self.user_cart.items():
            price = self.store_inventory[item]['individual_price']
            subtotal += price * quantity
            print(f"{item}: {quantity} at ${price:.2f} each.")
        print(f"Subtotal: ${subtotal:.2f}")

    def remove(self, item, quantity):
        if item in self.user_cart:
            if self.user_cart[item] >= quantity:
                self.user_cart[item] -= quantity
                self.store_inventory[item]['stock_quantity'] += quantity
                print(f"Removed {quantity} {item}(s) from your cart.")
                if self.user_cart[item] == 0:  # Remove item from cart if quantity reaches zero
                    del self.user_cart[item]
            else:
                print("Not enough items in your cart to remove that many.")
        else:
            print("Item not found in your cart.")

run = True

# Store Inventory Dictionary
store_inventory = {
    'Apples': {'stock_quantity': 1500, 'individual_price': 1.00},
    'Oranges': {'stock_quantity': 2000, 'individual_price': 0.75},
    'Bananas (Individual)': {'stock_quantity': 100, 'individual_price': 0.30},
    'Grapes (1 Ib bag)': {'stock_quantity': 2000, 'individual_price': 6.50},
    'Milk': {'stock_quantity': 150, 'individual_price': 3.50},
    'Bread': {'stock_quantity': 140, 'individual_price': 4.50},
    'Eggs (Dozen)': {'stock_quantity': 129, 'individual_price': 3.25},
    'Chicken Breast (1 Ib Bag)': {'stock_quantity': 550, 'individual_price': 7.50},
    'Rice': {'stock_quantity': 1000, 'individual_price': 0.50},
    'Pasta (Box)': {'stock_quantity': 800, 'individual_price': 0.50}
}

# Initialize the Store
store = Store(store_inventory)

# Main loop
while run:
    print("\nWelcome to Cosco Warehouse Inventory!\n"
          "1. Add Item\n"
          "2. Remove Item\n"
          "3. View Inventory\n"
          "4. View Cart and Subtotal\n"
          "5. Exit")

    try:
        user_input = int(input("Select an Action: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match user_input:
        case 1:
            store.display_store_inventory()
            item = input("What item would you like to add to the cart?: ")
            try:
                quantity = int(input("Enter the quantity: "))
                store.add(item, quantity)
            except ValueError:
                print("Please enter a valid quantity.")

        case 2:
            store.display_user_cart()
            item = input("Which item would you like to remove from your cart?: ")
            try:
                quantity = int(input("Enter the quantity: "))
                store.remove(item, quantity)
            except ValueError:
                print("Please enter a valid quantity.")

        case 3:
            store.display_store_inventory()  # Show inventory

        case 4:
            store.display_user_cart()  # Show cart and subtotal

        case 5:
            print("Thank you for visiting Cosco Warehouse Inventory!")
            run = False
            sys.exit()

        case _:
            print("Invalid selection, please try again.")

    main_menu = input("Would you like to return to the main menu (Y/N)?: ").lower()
    if main_menu == "n":
        run = False
