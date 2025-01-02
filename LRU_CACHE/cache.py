from lru_policy import LruPolicy
from hashmap_store import HashMapStore
from exceptions.storage_full_exception import StorageFullException
from exceptions.not_found_exception import NotFoundException

class Cache:
    def __init__(self, evictionPolicy: LruPolicy, storage: HashMapStore) -> None:
        self.evictionPolicy = evictionPolicy
        self.storage = storage

    # 2 methods GET and PUT
    def put(self, key, value):
        try:
            self.storage.add_to_store(key, value)
            self.evictionPolicy.get_key_or_create_new_key(key)
        except StorageFullException as s:
            remove_key = self.evictionPolicy.remove_lru_key()
            if remove_key == None:
                raise RuntimeError("unexpected issue!!")
            self.storage.remove_from_store(remove_key)
            self.put(key, value)

    def get(self, key):
        try:
            value = self.storage.get(key)
            self.evictionPolicy.get_key_or_create_new_key(key)
            return value
        except NotFoundException as nfe:
            return None
        




    