from enum import Enum

from abc import ABC

class BookFormat(Enum):
    HARDCOVER, EBOOK, AUDIO_BOOK, MAGAZINE, JOURNAL = 1,2,3,4,5

class Person:
    def __init__(self, name, address, email, phone):
        pass

class Address:
    def __init__(self, location, country, zipcode, city, state, streetAddress):
        pass

class ReservationStatus(Enum):
    COMPLETED, WAITING, CANCELLED, NONE = 1,2,3,4

class BookStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST = 1,2,3, 4

class AccountStatus(Enum):
    ACTIVE, BLACKLISTED, CLOSED = 1, 2, 3

class LibConstants:
    MAXIMUM_BOOKS_LENT = 5
    MAXIMUM_LENDING_DAYS = 30
    MAX_RESERVATION_DAYS = 5
    
