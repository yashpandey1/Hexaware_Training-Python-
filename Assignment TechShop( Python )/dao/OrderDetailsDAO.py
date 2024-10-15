from abc import ABC, abstractmethod
from entity.OrderDetails import OrderDetail

class OrderDetailDAO(ABC):
    @abstractmethod
    def add_order_detail(self, order_detail: OrderDetail):
        pass

    @abstractmethod
    def get_order_detail(self, order_detail_id: int) -> OrderDetail:
        pass

    @abstractmethod
    def update_order_detail(self, order_detail: OrderDetail):
        pass

    @abstractmethod
    def delete_order_detail(self, order_detail_id: int):
        pass
