
import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\Assignment TechShop( Python )")


from dao.DAOImplementation import DAOImplementation
from entity.Customer import Customer
from entity.Product import Product
from entity.Order import Order
from entity.OrderDetails import OrderDetail
from entity.Inventory import Inventory
from datetime import datetime
from exception.InvalidDataException import InvalidDataException
from exception.SqlException import SqlException

def main():
    dao = DAOImplementation()

    while True:
        try:
            print("\nTechShop Management System")
            print("1. Customer Management")
            print("2. Product Management")
            print("3. Order Management")
            print("4. Inventory Management")
            print("5. Sales Reporting")
            print("6. Payment Processing")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\nCustomer Management")
                print("1. Add Customer")
                print("2. View Customer")
                print("3. Update Customer")
                print("4. Delete Customer")
                print("5. List All Customers")
                customer_choice = input("Enter your choice: ")

                if customer_choice == "1":
                    # Add Customer
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    email = input("Enter email: ")
                    phone = input("Enter phone: ")
                    address = input("Enter address: ")
                    customer = Customer(None, first_name, last_name, email, phone, address)
                    dao.add_customer(customer)

                elif customer_choice == "2":
                    # View Customer
                    customer_id = int(input("Enter customer ID: "))
                    customer = dao.get_customer(customer_id)
                    if customer:
                        details = customer.get_customer_details()
                        print(f"Customer Details: {details}")
                    else:
                        print("Customer not found.")

                elif customer_choice == "3":
                    # Update Customer
                    customer_id = int(input("Enter customer ID to update: "))
                    customer = dao.get_customer(customer_id)
                    if customer:
                        customer.first_name = input("Enter new first name: ") or customer.first_name
                        customer.last_name = input("Enter new last name: ") or customer.last_name
                        customer.email = input("Enter new email: ") or customer.email
                        customer.phone = input("Enter new phone: ") or customer.phone
                        customer.address = input("Enter new address: ") or customer.address
                        dao.update_customer(customer)

                elif customer_choice == "4":
                    # Delete Customer
                    customer_id = int(input("Enter customer ID to delete: "))
                    dao.delete_customer(customer_id)

                elif customer_choice == "5":
                    # List All Customers
                    customers = dao.list_all_customers()
                    for cust in customers:
                        print(cust.get_customer_details())

                else:
                    print("Invalid choice. Please try again.")

            elif choice == "2":
                print("\nProduct Management")
                print("1. Add Product")
                print("2. View Product")
                print("3. Update Product")
                print("4. Delete Product")
                print("5. List All Products")
                product_choice = input("Enter your choice: ")

                if product_choice == "1":
                    # Add Product
                    name = input("Enter product name: ")
                    description = input("Enter product description: ")
                    price = float(input("Enter product price: "))
                    product = Product(None, name, description, price)
                    dao.add_product(product)

                elif product_choice == "2":
                    # View Product
                    product_id = int(input("Enter product ID: "))
                    product = dao.get_product(product_id)
                    if product:
                        details = product.get_product_details()
                        print(f"Product Details: {details}")
                    else:
                        print("Product not found.")

                elif product_choice == "3":
                    # Update Product
                    product_id = int(input("Enter product ID to update: "))
                    if product_id:
                        name = input("Enter new product name: ") 
                        description = input("Enter new product description: ") 
                        price = float(input("Enter new product price: ") )
                        dao.update_product(name, description, price, product_id)

                elif product_choice == "4":
                    # Delete Product
                    product_id = int(input("Enter product ID to delete: "))
                    dao.delete_product(product_id)

                elif product_choice == "5":
                    # List All Products
                    products = dao.list_all_products()
                    for prod in products:
                        print(prod.get_product_details())

                else:
                    print("Invalid choice. Please try again.")

            elif choice == "3":
                print("\nOrder Management")
                print("1. Add Order")
                print("2. Update Order Status")
                print("3. Remove Order")
                print("4. List All Orders")
                order_choice = input("Enter your choice: ")

                if order_choice == "1":
                    # Add Order
                    customer_id = int(input("Enter customer ID: "))
                    cursor = dao.connection.cursor()
                    cursor.execute("INSERT INTO Orders (CustomerID) VALUES (?)", (customer_id,))
                    # Retrieve the last inserted order ID using SCOPE_IDENTITY()
                    cursor.execute("SELECT SCOPE_IDENTITY()")
                    order_id = cursor.fetchone()[0]
                    dao.connection.commit()
                    order = Order(None, dao.get_customer(customer_id), datetime.now()) 

                    while True:
                        product_id = int(input("Enter product ID to order (or -1 to finish): "))
                        if product_id == -1:
                            break
                        quantity = int(input("Enter quantity: "))
                        dao.add_order_detail(order_id, product_id, quantity)
                    print("Order placed successfully.")

                elif order_choice == "2":
                    # Update Order Status
                    order_id = int(input("Enter order ID: "))
                    status = input("Enter new status (e.g., Processing, Shipped): ")
                    dao.update_order_status(order_id, status)

                elif order_choice == "3":
                    # Remove Order
                    order_id = int(input("Enter order ID to remove: "))
                    dao.delete_order(order_id)

                elif order_choice == "4":
                    # List All Orders
                    dao.list_all_orders() 

            elif choice == "4":
                print("\nInventory Management")
                print("1. Add Inventory Item")
                print("2. Update Inventory Item")
                print("3. Remove Inventory Item")
                print("4. List All Inventory Items")
                inventory_choice = input("Enter your choice: ")

                if inventory_choice == "1":
                    # Add Inventory Item
                    product_id = int(input("Enter product ID: "))  # Ensure this is an integer
                    quantity = int(input("Enter quantity to add: "))  # Ensure this is also an integer

                    try:
                        dao.add_inventory_item(product_id, quantity)  # Ensure you're calling the method correctly
                        print("Inventory item added successfully.")
                    except SqlException as e:
                        print(f"Database Error: {e}")

                elif inventory_choice == "2":
                    # Update Inventory Item
                    inventory_id = int(input("Enter inventory ID to update: "))
                    new_quantity = int(input("Enter new quantity: "))
                    try:
                        cursor = dao.connection.cursor()
                        # Fetch the current inventory item
                        cursor.execute("SELECT * FROM Inventory WHERE InventoryID = ?", (inventory_id,))
                        row = cursor.fetchone()
                        if row:
                            # Print current details (optional)
                            print(f"Current Quantity: {row.QuantityInStock}")
                            
                            # Update the inventory item in the database
                            dao.update_inventory_item(inventory_id, new_quantity)
                            print("Inventory item updated successfully.")
                        else:
                            print("Inventory item not found.")
                    except SqlException as e:
                        print(f"Database Error: {e}")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")

                elif inventory_choice == "3":
                    # Remove Inventory Item
                    inventory_id = int(input("Enter inventory ID to remove: "))
                    dao.delete_inventory(inventory_id)

                elif inventory_choice == "4":
                    # List All Inventory Items
                    cursor = dao.connection.cursor()
                    cursor.execute("SELECT * FROM Inventory")
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)

                else:
                    print("Invalid choice. Please try again.")

            elif choice == "5":
                print("\nSales Reporting")
                dao.generate_sales_report()

            elif choice == "6":
                order_id = int(input("Enter order ID for payment: "))
                # Verify if the order exists
                order = dao.get_order(order_id)
                if order:
                    payment_method = input("Enter payment method (e.g., Credit Card, PayPal): ")
                    amount = float(input("Enter payment amount: "))
                    dao.process_payment(order_id, payment_method, amount)
                    dao.update_order_status(order_id, "Paid")  # Update the order status after payment
                else:
                    print("Order not found. Please enter a valid Order ID.")
            
            elif choice == "7":
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")

        except InvalidDataException as e:
            print(f"Input Error: {e}")
        except SqlException as e:
            print(f"Database Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
