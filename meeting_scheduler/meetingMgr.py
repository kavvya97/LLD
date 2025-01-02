from meeting import Meeting
class MeetingMgr:
    _instance = None
    def __new__(cls) -> 'MeetingMgr':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.meetings = {}

    @classmethod
    def get_instance(cls) ->'MeetingMgr':
        return cls._instance

    def get_meetings(self, meeting_id):
        return self.meetings.get(meeting_id)
    
    def set_meetings(self, meeting_id, meeting: Meeting):
        self.meetings[meeting_id] = meeting