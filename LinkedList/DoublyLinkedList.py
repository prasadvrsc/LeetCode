class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_before(self, node, note_to_insert):
        if node_to_insert == self.head and note_to_insert == self.tail:
            return
        
    
    
    
    def remove_node_with_value(self,value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next    
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    
    def remove(self, node):
        if node == self.head:
            self.head.next
        if node ==self.tail:
            self.tail = self.tail.prev
        self.remove_bindings(node)    
    
    
    def contains_node_with_value(self, value):
        node = self.head
        while node is not None and node.value!=value:
            node = node.next
        return node is not None
    
    def remove_bindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
