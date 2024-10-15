from abc import ABC, abstractmethod

class CustomerDAO(ABC):
    @abstractmethod
    def add_customer(self, customer):
        pass

    @abstractmethod
    def get_customer(self, customer_id):
        pass

    @abstractmethod
    def update_customer(self, customer):
        pass

    @abstractmethod
    def delete_customer(self, customer_id):
        pass
