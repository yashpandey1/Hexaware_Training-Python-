from datetime import datetime

class Order:
    def __init__(self, order_id, customer, order_date=None, total_amount=0.0):
        self._order_id = order_id
        self._customer = customer
        self._order_date = order_date or datetime.now()
        self._total_amount = total_amount

    # Getter and Setter methods
    @property
    def order_id(self):
        return self._order_id

    @property
    def customer(self):
        return self._customer

    @property
    def order_date(self):
        return self._order_date

    @property
    def total_amount(self):
        return self._total_amount
    
    def get_order_details(self):
        order_details_list = [
            {
                "Product": detail.product.product_name,
                "Quantity": detail.quantity,
                "Subtotal": detail.calculate_subtotal()
            }
            for detail in self._order_details
        ]
        return {
            "OrderID": self._order_id,
            "Customer": self._customer.get_customer_details(),
            "OrderDate": self._order_date,
            "OrderDetails": order_details_list,
            "TotalAmount": self.calculate_total_amount()
        }
