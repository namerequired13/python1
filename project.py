# Inventory list to store all items
inventory = []

# -----------------------------
# Add Item
# -----------------------------
def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print(f"{name} added successfully!\n")


# -----------------------------
# Update Item
# -----------------------------
def update_item():
    name = input("Enter the name of the item to update: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("Item found. Enter new details:")

            item["price"] = float(input("New price: "))
            item["quantity"] = int(input("New quantity: "))
            item["category"] = input("New category: ")

            print(f"{name} updated successfully!\n")
            return

    print("Item not found.\n")


# -----------------------------
# View Inventory
# -----------------------------
def view_inventory():
    if not inventory:
        print("Inventory is empty.\n")
        return

    print("\n--- Inventory Items ---")
    for item in inventory:
        print(f"Name: {item['name']}")
        print(f"Price: ${item['price']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Category: {item['category']}")
        print("------------------------")
    print()


# -----------------------------
# Remove Item
# -----------------------------
def remove_item():
    name = input("Enter the name of the item to remove: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"{name} removed successfully!\n")
            return

    print("Item not found.\n")


# -----------------------------
# Search by Category
# -----------------------------
def search_by_category():
    category = input("Enter category to search: ")

    found_items = [item for item in inventory if item["category"].lower() == category.lower()]

    if not found_items:
        print("No items found in this category.\n")
        return

    print(f"\n--- Items in category '{category}' ---")
    for item in found_items:
        print(f"Name: {item['name']}")
        print(f"Price: ${item['price']}")
        print(f"Quantity: {item['quantity']}")
        print("------------------------")
    print()


# -----------------------------
# Main Program Loop
# -----------------------------
def main():
    while True:
        print("=== Market Inventory System ===")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
main()

