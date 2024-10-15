class Product:
    def __init__(self, product_id, name, description, price):
        self._product_id = product_id
        self._name = name
        self._description = description
        self._price = price

    # Getter and Setter methods
    def name(self):
        return self._name


    def name(self, value):
        self._name = value


    def description(self):
        return self._description


    def description(self, value):
        self._description = value


    def price(self):
        return self._price


    def price(self, value):
        self._price = value


    def product_id(self):
        return self._product_id 
    

    def get_product_details(self) -> dict:
        """Retrieve and display detailed information about the product."""
        return {
            "ProductID": self._product_id,
            "ProductName": self._name,
            "Description": self._description,
            "Price": self._price
        }

    def update_product_info(self, name=None, description=None, price=None):
        """Allow updates to product details."""
        if name:
            self._name = name
        if description:
            self._description = description
        if price is not None:
            self._price = price  # Allowing None to be a valid input to avoid confusion with 0

    def is_product_in_stock(self, inventory_list) -> bool:
        """Check if the product is currently in stock."""
        return any(inventory.product.product_id == self._product_id and inventory.quantity_in_stock > 0 for inventory in inventory_list)

