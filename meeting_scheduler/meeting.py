class Meeting:
    def __init__(self, meeting_id, creator, description, subject, participants=None,
                 day_of_meeting=None, start_time=None, end_time=None, is_recurring=None):
        self.id = meeting_id
        self.creator = creator
        self.description = description
        self.subject = subject
        self.participants = participants if participants is not None else []
        self.day_of_meeting = day_of_meeting
        self.start_time = start_time
        self.end_time = end_time
        self.is_recurring = is_recurring
        self.suggested_timings = []

    def display(self):
        print("------------------------------------------")
        print(f"Meeting details for meeting id {self.id} -")
        print(f"Subject - {self.subject}")
        print(f"Description - {self.description}")
        print(f"Organiser - {self.creator.get_name()}")
        print("Participants -", end=" ")
        for participant in self.participants:
            print(participant.get_name(), end=" ")
        print("\n------------------------------------------")

    def get_id(self):
        return self.id

    def get_organiser(self):
        return self.creator

    def get_description(self):
        return self.description

    def get_subject(self):
        return self.subject

    def get_day_of_meeting(self):
        return self.day_of_meeting

    def get_participants(self):
        return self.participants

    def get_suggested_timings(self):
        return self.suggested_timings

    def set_id(self, meeting_id):
        self.id = meeting_id

    def set_creator(self, creator):
        self.creator = creator

    def set_description(self, description):
        self.description = description

    def set_subject(self, subject):
        self.subject = subject

    def set_day_of_meeting(self, day_of_meeting):
        self.day_of_meeting = day_of_meeting

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_is_recurring(self, is_recurring):
        self.is_recurring = is_recurring

    def set_suggested_timings(self, suggested_timings):
        self.suggested_timings = suggested_timings
