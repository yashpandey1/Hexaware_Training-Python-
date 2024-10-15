from abc import ABC, abstractmethod
from entity.Product import Product

class ProductDAO(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def update_product(self, product: Product):
        pass

    @abstractmethod
    def delete_product(self, product_id: int):
        pass
