from rider import Rider
from riderMgr import RiderMgr
from driver import Driver
from driverMgr import DriverMgr
from tripMgr import TripManager
from location import Location

def main():
    rider1 = Rider("Kavs", 1, 2)
    rider2 = Rider("Goks", 2, 3)
    riderMgr = RiderMgr.get_rider_manager_instance()
    riderMgr.add_rider(rider1)
    riderMgr.add_rider(rider2)

    driver1 = Driver("h1", 1, 3)
    driver2 = Driver("h2", 2, 5)
    driverMgr = DriverMgr.get_driver_manager_instance()
    driverMgr.add_driver(driver1)
    driverMgr.add_driver(driver2)

    tripMgr = TripManager.get_tripMgr_instance()
    src_loc = Location(10, 10)
    dst_loc = Location(30, 30)
    tripMgr.create_trip(src_loc, dst_loc, rider1)

    tripsMap = tripMgr.get_trips_map()
    for trip_id in tripsMap:
        trip = tripMgr.get_trip_details(trip_id)
        trip.display_trip_details()

if __name__ == "__main__":
    main()
