from constants import PackageSize

class Package:
    def __init__(self, size, address, package_id) -> None:
        self.__size = size
        self.__address = address
        self.__package_id = package_id
        self.__pickup_expiry_date = None
        
    def get_package_size(self):
        return self.__size
    
    def get_package_id(self):
        return self.__package_id
    
    def set_pickup_expiry_date(self, due_date):
        self.__pickup_expiry_date = due_date
