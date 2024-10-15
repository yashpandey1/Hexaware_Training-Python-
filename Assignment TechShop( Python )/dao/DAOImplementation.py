
import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\Assignment TechShop( Python )")


import sys
import pyodbc
from dao.CustomerDAO import CustomerDAO
from dao.ProductDAO import ProductDAO
from dao.OrderDAO import OrderDAO
from dao.OrderDetailsDAO import OrderDetailDAO
from dao.InventoryDAO import InventoryDAO
from entity.Customer import Customer
from entity.Product import Product
from entity.Order import Order
from entity.OrderDetails import OrderDetail
from entity.Inventory import Inventory
from util.db_conn_util import DBConnUtil
from exception.InvalidDataException import InvalidDataException
from exception.SqlException import SqlException

class DAOImplementation(CustomerDAO, ProductDAO, OrderDAO, OrderDetailDAO, InventoryDAO):
    def __init__(self):
        self.connection = DBConnUtil.get_db_conn()

    def update_inventory_item(self, inventory_id: int, new_quantity: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Inventory SET QuantityInStock = ? WHERE InventoryID = ?", (new_quantity, inventory_id))
            self.connection.commit()
        except pyodbc.Error as e:
            raise SqlException(f"Error updating inventory item: {e}")
    def add_customer(self, customer: Customer):
        try:
            if not customer.email or "@" not in customer.email:
                raise InvalidDataException("Invalid email address provided.")
            if len(customer.phone) < 10:
                raise InvalidDataException("Phone number must be at least 10 digits.")
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Customers WHERE Email = ?", (customer.email,))
            if cursor.fetchone():
                raise InvalidDataException("Email already exists.")

            cursor.execute("INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?)",
                           (customer.first_name, customer.last_name, customer.email, customer.phone, customer.address))
            self.connection.commit()
            print("Customer added successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error adding customer: {e}")

    def list_all_customers(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Customers")
            rows = cursor.fetchall()
            customers = []
            for row in rows:
                customer = Customer(row.CustomerID, row.FirstName, row.LastName, row.Email, row.Phone, row.Address)
                customers.append(customer)
            return customers
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching customers: {e}")

    def get_customer(self, customer_id: int) -> Customer:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
            row = cursor.fetchone()
            if row:
                return Customer(row.CustomerID, row.FirstName, row.LastName, row.Email, row.Phone, row.Address)
            else:
                raise InvalidDataException("Customer not found.")
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching customer: {e}")

    def update_customer(self, customer: Customer):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Customers SET FirstName = ?, LastName = ?, Email = ?, Phone = ?, Address = ? WHERE CustomerID = ?",
                           (customer.first_name, customer.last_name, customer.email, customer.phone, customer.address, customer.customer_id))
            self.connection.commit()
            print("Customer updated successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error updating customer: {e}")

    def delete_customer(self, customer_id: int):
        try:
            cursor = self.connection.cursor()
            delete_orderdetails_query = f"DELETE FROM OrderDetails WHERE OrderID = (Select OrderID from Orders where CustomerID = {customer_id})"
            cursor.execute(delete_orderdetails_query)
            delete_orders_query = f"DELETE FROM Orders WHERE CustomerID = {customer_id}"
            cursor.execute(delete_orders_query)
            cursor.execute("DELETE FROM Customers WHERE CustomerID = ?", (customer_id,))
            self.connection.commit()
            print("Customer deleted successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error deleting customer: {e}")

    # Product DAO Implementation
    def add_product(self, product: Product):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Products (ProductName, Description, Price) VALUES (?, ?, ?)",
                           (product.name, product.description, product.price))
            self.connection.commit()
            print("Product added successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error adding product: {e}")

    def list_all_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()
            products = []
            for row in rows:
                product = Product(row.ProductID, row.ProductName, row.Description, row.Price)
                products.append(product)
            return products
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching products: {e}")

    def get_product(self, product_id: int) -> Product:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
            row = cursor.fetchone()
            if row:
                return Product(row.ProductID, row.ProductName, row.Description, row.Price)
            else:
                raise InvalidDataException("Product not found.")
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching product: {e}")

    def update_product(self, name, desc, price, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Products SET ProductName = ?, Description = ?, Price = ? WHERE ProductID = ?",
                           (name, desc, price, id))
            self.connection.commit()
            print("Product updated successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error updating product: {e}")

    def delete_product(self, product_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Inventory WHERE ProductID = ?", (product_id,))
            cursor.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
            self.connection.commit()
            print("Product deleted successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error deleting product: {e}")

    # Order DAO Implementation
    def add_order(self, order: Order):
        try:
            if not order.customer:
                raise InvalidDataException("Order must have a valid customer.")

            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Orders (CustomerID, OrderDate) VALUES (?, ?)",
                           (order.customer.customer_id, order.order_date))
            self.connection.commit()
            print("Order added successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error adding order: {e}")

    def list_all_orders(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Orders")
            rows = cursor.fetchall()
            
            # Print details of each order
            for row in rows:
                customer = self.get_customer(row.CustomerID)
                print(f"Order ID: {row.OrderID}, Customer: {customer.first_name + customer.last_name}, Order Date: {row.OrderDate}")
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching orders: {e}")

    def get_order(self, order_id: int) -> Order:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Orders WHERE OrderID = ?", (order_id,))
            row = cursor.fetchone()
            if row:
                customer = self.get_customer(row.CustomerID)
                return Order(row.OrderID, customer, row.OrderDate)
            else:
                raise InvalidDataException("Order not found.")
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching order: {e}")

    def update_order(self, order: Order):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Orders SET CustomerID = ?, OrderDate = ? WHERE OrderID = ?",
                           (order.customer.customer_id, order.order_date, order.order_id))
            self.connection.commit()
            print("Order updated successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error updating order: {e}")

    def delete_order(self, order_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Orders WHERE OrderID = ?", (order_id,))
            self.connection.commit()
            print("Order deleted successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error deleting order: {e}")

    def update_order_status(self, order_id: int, status: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Orders SET Status = ? WHERE OrderID = ?", (status, order_id))
            self.connection.commit()
            print("Order status updated successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error updating order status: {e}")

    # Inventory DAO Implementation
    def add_inventory(self, inventory: Inventory):
        try:
            if inventory.quantity_in_stock < 0:
                raise InvalidDataException("Quantity in stock cannot be negative.")

            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate) VALUES (?, ?, ?)",
                           (inventory.product.product_id, inventory.quantity_in_stock, inventory.last_stock_update))
            self.connection.commit()
            print("Inventory item added successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error adding inventory: {e}")

    def get_inventory(self, inventory_id: int) -> Inventory:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Inventory WHERE InventoryID = ?", (inventory_id,))
            row = cursor.fetchone()
            if row:
                product = self.get_product(row.ProductID)
                return Inventory(row.InventoryID, product, row.QuantityInStock, row.LastStockUpdate)
            else:
                raise InvalidDataException("Inventory item not found.")
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching inventory: {e}")

    def update_inventory(self, inventory: Inventory):
        try:
            if inventory.quantity_in_stock < 0:
                raise InvalidDataException("Updated quantity cannot be negative.")

            cursor = self.connection.cursor()
            cursor.execute("UPDATE Inventory SET QuantityInStock = ?, LastStockUpdate = ? WHERE InventoryID = ?",
                           (inventory.quantity_in_stock, inventory.last_stock_update, inventory.inventory_id))
            self.connection.commit()
            print("Inventory updated successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error updating inventory: {e}")

    def delete_inventory(self, inventory_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Inventory WHERE InventoryID = ?", (inventory_id,))
            self.connection.commit()
            print("Inventory item deleted successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error deleting inventory: {e}")

    def generate_sales_report(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Orders")
            orders = cursor.fetchall()
            for order in orders:
                print(f"Order ID: {order.OrderID}, Customer ID: {order.CustomerID}, Total Amount: {order.TotalAmount}")
        except pyodbc.Error as e:
            raise SqlException(f"Error generating sales report: {e}")

    def search_products(self, search_term: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Products WHERE ProductName LIKE ?", ('%' + search_term + '%',))
            products = cursor.fetchall()
            for product in products:
                print(f"Product ID: {product.ProductID}, Name: {product.ProductName}, Price: {product.Price}")
        except pyodbc.Error as e:
            raise SqlException(f"Error searching for products: {e}")
        
    def add_order_detail(self, order_id: int, product_id: int, quantity: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (?, ?, ?)",
                (order_id, product_id, quantity)
            )
            self.connection.commit()
        except pyodbc.Error as e:
            raise SqlException(f"Error adding order detail: {e}")

    def get_order_detail(self, order_detail_id: int) -> OrderDetail:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM OrderDetails WHERE OrderDetailID = ?", (order_detail_id,))
            row = cursor.fetchone()
            if row:
                order = self.get_order(row.OrderID)  # Fetch the order for this detail
                product = self.get_product(row.ProductID)  # Fetch the product for this detail
                return OrderDetail(row.OrderDetailID, order, product, row.Quantity)
            else:
                raise InvalidDataException("Order detail not found.")
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching order detail: {e}")

    def update_order_detail(self, order_detail: OrderDetail):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE OrderDetails SET OrderID = ?, ProductID = ?, Quantity = ? WHERE OrderDetailID = ?",
                           (order_detail.order.order_id, order_detail.product.product_id, order_detail.quantity, order_detail.order_detail_id))
            self.connection.commit()
            print("Order detail updated successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error updating order detail: {e}")

    def delete_order_detail(self, order_detail_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM OrderDetails WHERE OrderDetailID = ?", (order_detail_id,))
            self.connection.commit()
            print("Order detail deleted successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error deleting order detail: {e}")
        
    def get_order_with_details(self, order_id: int) -> Order:
        try:
            cursor = self.connection.cursor()
            
            # Fetch the main order details
            cursor.execute("SELECT * FROM Orders WHERE OrderID = ?", (order_id,))
            order_row = cursor.fetchone()
            
            if not order_row:
                raise InvalidDataException("Order not found.")

            # Fetch customer details
            customer = self.get_customer(order_row.CustomerID)

            # Prepare to store order details
            order_details_list = []

            # Fetch order details associated with this order
            cursor.execute("SELECT * FROM OrderDetails WHERE OrderID = ?", (order_id,))
            order_details_rows = cursor.fetchall()

            for detail_row in order_details_rows:
                product = self.get_product(detail_row.ProductID)  # Fetch the product
                order_details_list.append({
                    "ProductID": product.product_id,
                    "ProductName": product.name,
                    "Quantity": detail_row.Quantity,
                    "Subtotal": detail_row.Quantity * product.price  # Calculate subtotal
                })
            
            # Return a comprehensive dictionary
            return {
                "OrderID": order_row.OrderID,
                "Customer": customer.get_customer_details(),
                "OrderDate": order_row.OrderDate,
                "OrderDetails": order_details_list
            }
        except pyodbc.Error as e:
            raise SqlException(f"Error fetching order with details: {e}")
        
    def process_payment(self, order_id: int, payment_method: str, amount: float):
        try:
            if amount <= 0:
                raise InvalidDataException("Payment amount must be greater than zero.")
            
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Payments (OrderID, Amount, PaymentMethod) VALUES (?, ?, ?)",
                        (order_id, amount, payment_method))
            self.connection.commit()
            print("Payment processed successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error processing payment: {e}")

    def update_order_status(self, order_id: int, status: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Orders SET Status = ? WHERE OrderID = ?", (status, order_id))
            self.connection.commit()
            print("Order status updated successfully.")
        except pyodbc.Error as e:
            raise SqlException(f"Error updating order status: {e}")

    def add_inventory_item(self, product_id: int, quantity: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Inventory (ProductID, QuantityInStock) VALUES (?, ?)", (product_id, quantity))
            self.connection.commit()
        except pyodbc.Error as e:
            raise SqlException(f"Error adding inventory: {e}")