from enum import Enum

class PackageSize(Enum):
    SMALL, MEDIUM, LARGE = 0, 1, 2

class Address:
    def __init__(self, streetName, streetAddress, pincode) -> None:
        self.streetName = streetName
        self.pincode = pincode

class BoxSize(Enum):
    SMALL, MEDIUM, LARGE = 0, 1, 2