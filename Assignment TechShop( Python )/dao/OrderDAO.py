from abc import ABC, abstractmethod
from entity.Order import Order

class OrderDAO(ABC):
    @abstractmethod
    def add_order(self, order: Order):
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def update_order(self, order: Order):
        pass

    @abstractmethod
    def delete_order(self, order_id: int):
        pass

    @abstractmethod
    def update_order_status(self, order_id: int, status: str):
        pass
