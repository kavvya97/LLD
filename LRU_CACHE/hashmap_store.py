from exceptions.storage_full_exception import StorageFullException
from exceptions.not_found_exception import NotFoundException
class HashMapStore:
    def __init__(self, capacity) -> None:
        self.store = {}
        self.capacity = capacity

    def add_to_store(self, key, value):
        if self.is_store_full():
            raise StorageFullException("storage full!")
        self.store[key] = value

    def remove_from_store(self, key):
        if key in self.store:
            del self.store[key]
        else:
            raise NotFoundException("Key not found!")
        
    def get(self, key):
        if key not in self.store:
            raise NotFoundException("Key not found!")
        return self.store[key]

    def is_store_full(self):
        return  self.capacity == len(self.store)