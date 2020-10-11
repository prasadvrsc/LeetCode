class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size or 1


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def set_head_to(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head = self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()

    
class DoublyLinkedListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = next


        
