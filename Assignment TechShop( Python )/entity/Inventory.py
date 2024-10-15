from datetime import datetime

import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\Assignment TechShop( Python )")

from entity.Product import Product
from exception.InvalidDataException import InvalidDataException

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update=None):
        self._inventory_id = inventory_id
        self._product = product
        self._quantity_in_stock = quantity_in_stock
        self._last_stock_update = last_stock_update or datetime.now()

    # Getter and Setter methods
    @property
    def inventory_id(self):
        return self._inventory_id

    @property
    def product(self):
        return self._product

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @property
    def last_stock_update(self):
        return self._last_stock_update

    def get_product(self) -> Product:
        """A method to retrieve the product associated with this inventory item."""
        return self._product

    def get_quantity_in_stock(self) -> int:
        """A method to get the current quantity of the product in stock."""
        return self._quantity_in_stock

    def add_to_inventory(self, quantity: int):
        """A method to add a specified quantity of the product to the inventory."""
        self._quantity_in_stock += quantity
        self._last_stock_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Update the last stock update time

    def remove_from_inventory(self, quantity: int):
        """A method to remove a specified quantity of the product from the inventory."""
        if quantity > self._quantity_in_stock:
            raise InvalidDataException("Not enough stock to remove.")
        self._quantity_in_stock -= quantity
        self._last_stock_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_stock_quantity(self, new_quantity: int):
        """A method to update the stock quantity to a new value."""
        self._quantity_in_stock = new_quantity
        self._last_stock_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def is_product_available(self, quantity_to_check: int) -> bool:
        """A method to check if a specified quantity of the product is available in the inventory."""
        return self._quantity_in_stock >= quantity_to_check

    def get_inventory_value(self) -> float:
        """A method to calculate the total value of the products in the inventory based on their prices and quantities."""
        return self._quantity_in_stock * self._product.price

    def list_low_stock_products(self, threshold: int) -> list:
        """A method to list products with quantities below a specified threshold, indicating low stock."""
        if self._quantity_in_stock < threshold:
            return [self.product.get_product_details()]
        return []

    def list_out_of_stock_products(self) -> bool:
        """A method to list products that are out of stock."""
        return self._quantity_in_stock == 0

    def list_all_products(self) -> dict:
        """A method to list all products in the inventory, along with their quantities."""
        return {
            "ProductID": self._product.product_id,
            "ProductName": self._product.product_name,
            "QuantityInStock": self._quantity_in_stock
        }


    
