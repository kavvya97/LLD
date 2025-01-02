class DoublyLinkedListNode:
    def __init__(self, key, prev=None, next=None) -> None:
        self.key = key
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self) -> None:
        self.left = DoublyLinkedListNode(0)
        self.right = DoublyLinkedListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def add_new_node_to_last(self, node: DoublyLinkedListNode):
        prev_node = self.right.prev
        prev_node.next, self.right.prev = node, node
        node.next, node.prev = self.right, prev_node

    def add_new_element_to_last(self, element):
        if not element:
            return
        new_node = DoublyLinkedListNode(element)
        self.add_new_node_to_last(new_node)
        return new_node
    
    def get_lru(self):
        return self.left.next
    
    def remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        node.next, node.prev = None, None

    
        