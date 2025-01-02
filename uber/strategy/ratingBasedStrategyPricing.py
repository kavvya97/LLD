from tripMetaData import TripMetaData

class RatingBasedStrategyPricing:
    def determine_price(self, tripMetaData: TripMetaData):
        trip_meta_data = tripMetaData  # Renaming for clarity
        if trip_meta_data.isHighRating(trip_meta_data.get_driver_rating()):
            return 65.0
        else:
            return 55.0
