class Rider:
    def __init__(self, name, rider_id, rating) -> None:
        self.name = name
        self.rider_id = rider_id
        self.rating = rating

    def getRiderName(self):
        return self.name
    
    def getRiderId(self):
        return self.rider_id
    
    def getRiderRating(self):
        return self.rating