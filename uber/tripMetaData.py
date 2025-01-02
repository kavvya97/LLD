class TripMetaData:
    def __init__(self, src, dst, driver_rating, rider_rating) -> None:
        self.src = src
        self.dst = dst
        self.driver_rating = driver_rating
        self.rider_rating = rider_rating
    
    def get_driver_rating(self):
        return self.driver_rating
    
    def get_rider_rating(self):
        return self.rider_rating
    
    def isHighRating(self, driver_rating):
        if driver_rating >= 4:
            return True
        else:
            return False

    def set_driver_rating(self, rating):
        self.driver_rating = rating