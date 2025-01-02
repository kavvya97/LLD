class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        self.children = []
        self.is_directory = False if "." in self.name else True
        self.extension = self.name.split(".")[1] if "." in self.name else ""
    