class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_first(self, value):
        #No head node
        if self.head is None:
            self.head = Node(value)
        #if there is a node existing
        else:
            new_node = Node(value) #Create a new node
            new_node.next = self.head    # point new node next to current head
            self.head = new_node # point head to the new node
            
            

    def add_last(self, value):
        # If head is None - No LInked list 
        if self.head is None:
            self.head = Node(value)
        else: # 1 -> 2
            current = self.head
            while current.next is not None:
                current = current.next 
            current.next = Node(value)


    def add_after_value(self, initial_value, new_node_value):
        if self.head is None:
            return self.head
        else:
            current_node = self.head
            while current_node.next is not None:
                if(current_node.value == initial_value): 
                    temp = current_node.next
                    new_node = Node(new_node_value)
                    current_node.next = new_node
                    new_node.next = temp
                    break
                else:
                    current_node = current_node.next



    def remove(self, value):
        if self.head is None:
            return
        elif self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if (current.next.value == value):
                    temp = current.next.next
                    current.next = temp
                else:
                    current = current.next
            
        

    def print_linked_list(self):
        current_node = self.head
        #if head is None
        if current_node is None:
            print(self.head)

        while current_node is not None:
            print(current_node.value, end= ' ')
            current_node = current_node.next



# Test Case
new_linked_list = LinkedList()
new_linked_list.print_linked_list()
new_linked_list.add_last(1) # 1 
# new_linked_list.print_linked_list()
new_linked_list.add_last(2) # 1 -> 2
new_linked_list.add_last(3) # 1 -> 2 _3
new_linked_list.print_linked_list()
new_linked_list.add_first(0) # 1 -> 2 _3
new_linked_list.add_after_value(1, 22) # 0 1 22 2 3 

new_linked_list.add_after_value(55, 44)
new_linked_list.remove(22)

print()
new_linked_list.print_linked_list()





    
    