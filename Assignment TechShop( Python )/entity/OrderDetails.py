class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        self._order_detail_id = order_detail_id
        self._order = order
        self._product = product
        self._quantity = quantity

    # Getter and Setter methods
    @property
    def order_detail_id(self):
        return self._order_detail_id

    @property
    def order(self):
        return self._order

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity
    
    def calculate_subtotal(self) -> float:
        """Calculate the subtotal for this order detail."""
        return self._quantity * self._product.price

    def get_order_detail_info(self) -> dict:
        """Retrieve and display information about this order detail."""
        return {
            "OrderDetailID": self._order_detail_id,
            "Product": self._product.product_name,
            "Quantity": self._quantity,
            "Subtotal": self.calculate_subtotal()
        }

    def update_quantity(self, new_quantity: int):
        """Allows updating the quantity of the product in this order detail."""
        self._quantity = new_quantity
