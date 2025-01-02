# Librarian, user all of them will have a account
from abc import ABC, abstractmethod
import datetime
from constants import BookFormat, AccountStatus, Address, BookStatus, LibConstants, ReservationStatus
# Abstract class
class Account(ABC):
    def __init__(self, account_id, name, password, status=AccountStatus.ACTIVE):
        pass

    @abstractmethod
    def reset_password():
        pass

class Librarian(Account):
    def __init__(self, is_admin,status=AccountStatus.ACTIVE):
        super.__init__()
    
    def add_books(book: BookFormat) -> None:
        pass

    def block_member(memberId: int) -> int:
        pass

    def unblock_member(memberId: int) -> int:
        pass

class Member(Account):
    def __init__(self, id, password, person, status=AccountStatus.Active):
        super().__init__(id, password, person, status)
        self.member_id = id
        self.__date_of_membership = datetime.date.today()
        self.__total_books_checkedout = 0

    def get_member_id(self):
        return self.member_id
    
    def get_total_books(self):
        return self.__total_books_checkedout
    
    def reserve_book(self, bookId):
        pass

    def increment_checkouted_books(self):
        self.__total_books_checkedout += 1

    def decrement_checkouted_books(self):
        self.__total_books_checkedout -= 1

    def checkout_book(self, bookId):
        if self.__total_books_checkedout > LibConstants.MAXIMUM_BOOKS_LENT:
            raise ValueError(f"Users cannot borrow more than {LibConstants.MAXIMUM_BOOKS_LENT} books")
        book_reservation = BookReservation.getReservationStatus(bookId)
        # Another user has reserved the book
        if book_reservation != None and book_reservation.member_id != self.member_id:
            raise ValueError("The Book is currently reserved by another user. Please check again after 5 days")
        elif book_reservation != None:
            book_reservation.update_status(ReservationStatus.COMPLETED)
        
        self.increment_checkouted_books()
        return True
    
    def check_for_fine(self, bookId):
        details = BookLending.fetch_lending_details(bookId)
        due_date = details.get_due_date()
        current_date = datetime.date.today()
        if current_date > due_date:
            diff = current_date - due_date
            diff_days = diff.days
            Fine.updateFine(self.get_member_id())

    def return_book(self, bookId):

        """
        1. scan the bookId
        2. get the memberId and reduce the number of books that he has loaned
        3. check for fines and update the member account accordingly
        4. Check if the book is reserbed by any member
        5. if book is reserved, modify the status to RESERVED and notify the other member accoridingly else change
        status to AVAILABLe
        """
        member_id = self.get_member_id()
        reservation = BookReservation.getReservationStatus(bookId)
        if reservation.member_id != member_id:
            raise ValueError(f"Current user did not loan the book")
        self.check_for_fine(bookId=bookId)
        if reservation != None:
            BookItem.update_status(BookStatus.RESERVED)
            reservation.send_notification(bookId)
        else:
            BookItem.update_status(BookStatus.AVAILABLE)
        self.decrement_checkouted_books()



    def renew_book(self, bookId):
        """
        1. Check for fines
        2. Renew book allowed only if its not reserved
        3. if not send notification
        """
        member_id = self.get_member_id()
        self.check_for_fine(bookId)
        reservation = BookReservation.getReservationStatus(bookId)
        if reservation != None and reservation.member_id != self.get_member_id():
            BookItem.update_status(BookStatus.RESERVED)
            reservation.send_notification(bookId)
            raise ValueError("Current book cannot be renewed since it is being reserved by another member")
        BookItem.updateDueDate(datetime.date.now().AddDays(LibConstants.MAXIMUM_LENDING_DAYS))      
        return True      
            












    

