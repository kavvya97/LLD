import threading
from user import User
class OrderManager:
    _orderManagerInstance = None
    _mtx = threading.Lock()

    def __init__(self) -> None:
        self.order_list = {}
    
    @staticmethod
    def get_order_manager_instance():
        if OrderManager._orderManagerInstance is None:
            with OrderManager._mtx:
                if OrderManager._orderManagerInstance is None:
                    OrderManager._orderManagerInstance = OrderManager()
        return OrderManager._orderManagerInstance
    
    def get_order(self, orderId: int):
        return self.order_list[orderId]

