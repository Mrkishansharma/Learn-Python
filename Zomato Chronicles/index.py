class ZestyZomato:
    def __init__(self):
        self.menu = {}
        self.orders = {}
        self.order_id_counter = 1

    def add_dish(self, dish_id, name, price):
        self.menu[dish_id] = {'name': name, 'price': price, 'available': True}

    def remove_dish(self, dish_id):
        if dish_id in self.menu:
            del self.menu[dish_id]
            print(f"Dish {dish_id} removed from the menu.")
        else:
            print(f"Dish {dish_id} not found in the menu.")

    def update_dish_availability(self, dish_id, available):
        if dish_id in self.menu:
            self.menu[dish_id]['available'] = available
        else:
            print(f"Dish {dish_id} not found in the menu.")

    def take_order(self, customer_name, dish_ids):
        order_items = []
        total_price = 0

        for dish_id in dish_ids:
            if dish_id in self.menu and self.menu[dish_id]['available']:
                order_items.append(self.menu[dish_id]['name'])
                total_price += self.menu[dish_id]['price']
            else:
                print(f"Dish {dish_id} is not available.")

        if order_items:
            order_id = self.order_id_counter
            self.orders[order_id] = {'customer_name': customer_name, 'items': order_items, 'status': 'received', 'total_price': total_price}
            self.order_id_counter += 1
            print(f"Order placed with ID {order_id}. Total price: {total_price}")

    def update_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
            print(f"Order {order_id} status updated to '{status}'.")
        else:
            print(f"Order {order_id} not found.")

    def review_orders(self):
        for order_id, order in self.orders.items():
            print(f"Order ID: {order_id}, Customer: {order['customer_name']}, Items: {', '.join(order['items'])}, Status: {order['status']}, Total Price: {order['total_price']}")

    def view_menu(self):
        print("\nMenu:")
        for dish_id, dish_info in self.menu.items():
            availability = "Available" if dish_info['available'] else "Not Available"
            print(f"Dish ID: {dish_id}, Name: {dish_info['name']}, Price: {dish_info['price']}, Availability: {availability}")

    def run(self):
        while True:
            print("\nZesty Zomato Operations:")
            print("1. Add Dish")
            print("2. Remove Dish")
            print("3. Update Dish Availability")
            print("4. Take Order")
            print("5. Update Order Status")
            print("6. Review Orders")
            print("7. View Menu")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                dish_id = input("Enter dish ID: ")
                name = input("Enter dish name: ")
                price = float(input("Enter dish price: "))
                self.add_dish(dish_id, name, price)
            elif choice == '2':
                dish_id = input("Enter dish ID to remove: ")
                self.remove_dish(dish_id)
            elif choice == '3':
                dish_id = input("Enter dish ID to update availability: ")
                available = input("Enter availability (yes/no): ").lower() == 'yes'
                self.update_dish_availability(dish_id, available)
            elif choice == '4':
                customer_name = input("Enter customer name: ")
                dish_ids = input("Enter dish IDs (comma-separated): ").split(',')
                self.take_order(customer_name, dish_ids)
            elif choice == '5':
                order_id = int(input("Enter order ID to update status: "))
                status = input("Enter new status: ")
                self.update_order_status(order_id, status)
            elif choice == '6':
                self.review_orders()
            elif choice == '7':
                self.view_menu()
            elif choice == '8':
                print("Exiting Zesty Zomato.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    zesty_zomato = ZestyZomato()
    zesty_zomato.run()
