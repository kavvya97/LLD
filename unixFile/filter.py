from abc import ABC, abstractmethod
class Filter:
    def __init__(self) -> None:
        pass
    @abstractmethod
    def apply(self, filter):
        pass



