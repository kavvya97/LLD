from doublyLinkedList import DoublyLinkedList, DoublyLinkedListNode
class LruPolicy:
    def __init__(self) -> None:
        self.dll = DoublyLinkedList()
        self.map = {}

    def get_key_or_create_new_key(self, key):
        if key in self.map:
            node = self.map[key]
            self.dll.remove_node(node)
            self.dll.add_new_node_to_last(node)
        else:
            new_node = self.dll.add_new_element_to_last(key)
            self.map[key] = new_node

    def remove_lru_key(self):
        lru = self.dll.get_lru()
        if lru.key == None:
            return
        self.dll.remove_node(lru)
        return lru.key