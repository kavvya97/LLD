from package import Package
from constants import Address
from box import Box
from typing import List
from datetime import datetime, timedelta
class Locker:
    def __init__(self, address: Address, locker_id) -> None:
        self.locker_id = locker_id
        self.address = address
        self.boxes = []
        self.package_id_to_box_id = {}

    def add_boxes(self, box: Box):
        self.boxes.append(box)

    def remove_boxes(self, box: Box):
        self.boxes.pop(box)

    def is_locker_available(self):
        for box in self.boxes:
            if box.available:
                return True
        return False
    
    def assign_box_to_package(self, package: Package):
        if self.is_locker_available():
            package_size = package.get_package_size()
            available_boxes = [box for box in self.boxes if box.available]
            available_boxes.sort(key=lambda box: box.get_box_size())
            box_to_assign = None
            for box in available_boxes:
                if box.available and box.get_box_size() == package_size:
                    box.allocate_box()
                    box_to_assign = box
                    break
                    
            if not box_to_assign:
                for box in available_boxes:
                    if box.available and box.get_box_size() > package_size:
                        box_to_assign = box
                        break
            
            box_to_assign.allocate_box()
            self.package_id_to_box_id[package.get_package_id()] = box_to_assign.get_box_id()
            self.package.set_pickup_expiry_date(self, datetime.now() + timedelta(days=5))
            return box_to_assign.get_box_id()
        
        else:
            raise ValueError("Locker is Full!!")

    def get_package(self, package_id):
        if package_id in self.package_id_to_box_id:
            return self.package_id_to_box_id[package_id]
        raise ValueError("Invalid Package ID!")

    def detect_expired_packages(self):
        pass
