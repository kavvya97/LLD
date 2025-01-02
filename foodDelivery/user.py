from location import Location
class User:
    def __init__(self, userId, name, location: Location) -> None:
        self.name = name
        self.location = location
        self.user_id = userId

    def get_user_id(self):
        return self.user_id
    
    def get_user_location(self):
        return self.location
    
    def get_user_name(self):
        return self.name

