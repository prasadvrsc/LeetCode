from heapq import *

class ListNode(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    # def __lt__(self, other):
    #     return self.value < other.value

class Solution(object):
    def merge_two_lists(self, l1, l2):
        #Can also be implemented as lambda functions
        ListNode.__eq__ = lambda self, other: self.value == other.value
        ListNode.__lt__ = lambda self, other: self.value < other.value
        

        if l1 is None and l2 is None:
            return l1
        
        min_heap =[]
        result_head, result_tail = None, None
        
        if l1 is not None:
            heappush(min_heap, l1)
        if l2 is not None:
            heappush(min_heap, l2)
        
        while len(min_heap) > 0:
            current_node = heappop(min_heap)
            if result_head is None:
                result_head = current_node
                result_tail = current_node
            else:
                result_tail.next = current_node
                result_tail = current_node
            if current_node.next is not None:
                heappush(min_heap, current_node.next)
        return result_head

#Test Cases
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

result = Solution().merge_two_lists(list1,list2)
while result is not None:
    print(result.value, end = " ")
    result = result.next


#Test Case -2
list3 = None
list4 = None

result = Solution().merge_two_lists(list3,list4)
print(result)


