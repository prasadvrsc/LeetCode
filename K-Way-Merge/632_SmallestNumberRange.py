'''
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.
Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
'''
import math
from heapq import *

def find_smallest_range(lists):
    min_heap = []
    range_start, range_end = 0, math.inf
    current_max_number = -math.inf

    # Push the first element of each array in the min heap

    for arr in lists:
        heappush(min_heap, (arr[0], 0, arr))
        current_max_number = max(current_max_number, arr[0])

    #take the smallest element from the min-heap, if it gives us smaller range, update the ranges
    #if the array of the top element has more elements, insert the next element in the heap
    while(len(min_heap)==len(lists)):
        num, i ,arr = heappop(min_heap)
        if range_end - range_start > current_max_number - num:
            range_start = num
            range_end = current_max_number

        if len(arr) > i + 1:
            #insert the next element in to min heap
            heappush(min_heap, (arr[i+1], i+1, arr))
            current_max_number = max(current_max_number , arr[i+1])
    
    return [range_start, range_end]

print("Smallest range is: " +
    str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))
Result: [4,7]




