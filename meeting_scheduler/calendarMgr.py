from calendar import user_calendar
class CalendarMgr:
    def __init__(self):
        self.calendars = {}

    def get_calendar_for_user(self, user_name):
        # If the user has a calendar, return it; otherwise, create a new one and return it
        if user_name not in self.calendars:
            self.calendars[user_name] = user_calendar()
        return self.calendars[user_name] 