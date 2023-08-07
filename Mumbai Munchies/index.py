class Snack:
    def __init__(self, id, name, price, availability):
        self.id = id
        self.name = name
        self.price = price
        self.availability = availability

def add_snack(inventory):
    id = input("Enter snack ID: ")
    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    availability = input("Is the snack available (yes/no): ")
    
    snack = Snack(id, name, price, availability)
    inventory.append(snack)
    print("Snack added to inventory.")

def remove_snack(inventory):
    id = input("Enter snack ID to remove: ")
    for snack in inventory:
        if snack.id == id:
            inventory.remove(snack)
            print("Snack removed from inventory.")
            return
    print("Snack not found in inventory.")

def update_availability(inventory):
    id = input("Enter snack ID to update availability: ")
    availability = input("Update availability (yes/no): ")
    for snack in inventory:
        if snack.id == id:
            snack.availability = availability
            print("Availability updated.")
            return
    print("Snack not found in inventory.")

def record_sale(inventory, sales_records):
    id = input("Enter snack ID sold: ")
    for snack in inventory:
        if snack.id == id:
            if snack.availability == "yes":
                sales_records.append(snack)
                snack.availability = "no"
                print("Sale recorded.")
                return
            else:
                print("Snack is not available.")
                return
    print("Snack not found in inventory.")

def display_inventory(inventory):
    print("Snack Inventory:")
    for snack in inventory:
        print(f"ID: {snack.id}, Name: {snack.name}, Price: {snack.price}, Availability: {snack.availability}")

def display_sales_records(sales_records):
    print("Sales Records:")
    for snack in sales_records:
        print(f"ID: {snack.id}, Name: {snack.name}, Price: {snack.price}")

def main():
    inventory = []
    sales_records = []

    while True:
        print("\nWelcome to Mumbai Munchies Canteen")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Availability")
        print("4. Record Sale")
        print("5. Display Inventory")
        print("6. Display Sales Records")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_snack(inventory)
        elif choice == "2":
            remove_snack(inventory)
        elif choice == "3":
            update_availability(inventory)
        elif choice == "4":
            record_sale(inventory, sales_records)
        elif choice == "5":
            display_inventory(inventory)
        elif choice == "6":
            display_sales_records(sales_records)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
