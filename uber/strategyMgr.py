import threading
from tripMetaData import TripMetaData
from strategy.ratingBasedStrategyPricing import RatingBasedStrategyPricing
from strategy.leastTimeBasedMatchingStrategy import LeastTimeBasedMatchingStrategy

class StrategyMgr:

    strategyMgrInstance = None
    mtx = threading.Lock()
    
    @staticmethod
    def get_strategyMgr_instance():
        if StrategyMgr.strategyMgrInstance is None:
            with StrategyMgr.mtx:
                if StrategyMgr.strategyMgrInstance is None:
                    StrategyMgr.strategyMgrInstance = StrategyMgr()
        return StrategyMgr.strategyMgrInstance
    
    def determine_price_matching_strategy(self, tripMetadata: TripMetaData):
        return RatingBasedStrategyPricing().determine_price(tripMetadata)

    def determine_drive_matching_strategy(self,tripMetadata: TripMetaData):
        return LeastTimeBasedMatchingStrategy().match_driver(tripMetadata)

