'''
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
'''

from __future__ import print_function
from heapq import *

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value

# O(N*logK) Time N- total number of elements, K - number of input arrays
# O(K) Space
def merge_lists(lists):
    min_heap = []

    # put the root of each list in the min heap
    for root in lists:
        if root is not None:
            heappush(min_heap, root)
        
        
    # Take the smallest element from the min-heap and add it to the result
    # If the top element has next element add it to to the heap

    result_head, result_tail = None, None

    while min_heap:
        current_node = heappop(min_heap)
        if result_head is None:
            result_head, result_tail = current_node, current_node
        else:
            result_tail.next = current_node
            result_tail = result_tail.next  

        if current_node.next is not None:
            heappush(min_heap, current_node.next)

    return result_head


# Test Case
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

result = merge_lists([l1, l2, l3])

while result is not None:
    print(str(result.value)+ " " , end ='')
    result = result.next