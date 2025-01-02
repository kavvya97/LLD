
from filter import Filter
from file import File
class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def apply(self, file: File):
        return file.extension == self.extension