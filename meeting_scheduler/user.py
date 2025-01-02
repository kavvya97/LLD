from calendar import meeting_calendar
class User:
    def __init__(self, name, id, designation, calendar) -> None:
        self._name = name
        self._id = id
        self._designation = designation
        self._calendar = meeting_calendar()

    def display_calendar(self, day):
        self._calendar.displayCalendar(day)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_designation(self):
        return self.designation

    def get_calendar(self):
        return self.calendar

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_designation(self, designation):
        self.designation = designation
    
