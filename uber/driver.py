class Driver:
    def __init__(self, name, driver_id, rating) -> None:
        self.name = name
        self.driver_id = driver_id
        self.rating = rating

    def getDriverName(self):
        return self.name
    
    def getDriverId(self):
        return self.driver_id
    
    def getDriverRating(self):
        return self.rating