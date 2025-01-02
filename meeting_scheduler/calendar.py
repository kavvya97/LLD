from meetingMgr import MeetingMgr
class user_calendar:
    def __init__(self):
        self.day_meetings = {}

    def add_meeting(self, day, meeting_id):
        # Check if the day exists in the calendar, if not, create it
        if day not in self.day_meetings:
            self.day_meetings[day] = []
        # Add the meeting ID to the specified day
        self.day_meetings[day].append(meeting_id)

    def get_meetings(self, day):
        return self.day_meetings.get(day, [])  # Return an empty list if no meetings for the day

    def display(self, day):
        for meeting_id in self.day_meetings.get(day, []):
            meeting_mgr = MeetingMgr.get_instance()
            meeting = meeting_mgr.get_meeting(meeting_id)
            meeting.display()