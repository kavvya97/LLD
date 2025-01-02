from filter import Filter
from file import File

class MinSizeFilter(Filter):
    def __init__(self, size) -> None:
        self.size = size
    def apply(self, file: File):
        return file.size > self.size
