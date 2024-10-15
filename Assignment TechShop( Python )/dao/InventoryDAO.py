from abc import ABC, abstractmethod
from entity.Inventory import Inventory

class InventoryDAO(ABC):
    @abstractmethod
    def add_inventory(self, inventory: Inventory):
        pass

    @abstractmethod
    def get_inventory(self, inventory_id: int) -> Inventory:
        pass

    @abstractmethod
    def update_inventory(self, inventory: Inventory):
        pass

    @abstractmethod
    def delete_inventory(self, inventory_id: int):
        pass
