from filter import Filter
from file import File
class UnixFind:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter: Filter):
        self.filters.append(filter)

    def apply_OR_filtering(self, root: File):
        def dfs(root: File, res):
            if root.is_directory:
                for child in root.children:
                    dfs(child, res)
            else:
                for filter in self.filters:
                    if filter.apply(root):
                        res.append(root)
                        return
                
        res = []
        dfs(root, res)
        return res
    
    def apply_AND_filtering(self, root: File):
        def dfs(root: File, res):
            if root.is_directory:
                for child in root.children:
                    dfs(child, res)
            else:
                for filter in self.filters:
                    if not filter.apply(root):
                        return

                res.append(root)

        res = []
        dfs(root, res)
        return res