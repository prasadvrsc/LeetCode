'''
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, 
this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
'''

from heapq import *

# O(K*logM) Time where M - total number of input arrays
# O(M) Space
def find_Kth_smallest(lists, k):
    min_heap = []

    #Push the 1st element of each lists to the min heap
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))

    #Take the smallest element from teh min heap, 
    #if the running count is equal to k return the number
    number_count, value = 0, 0
    while min_heap:
        value, current_index, current_list = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break

        #if the array of the top element has more elements,
        #add the next element to the heap
        if len(current_list) > current_index + 1:
            heappush(min_heap, (current_list[current_index+1], current_index+1, current_list))

    return value



#Test Case:

print("Kth smallest number is: " +
    str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
# Result expect = 4


print("Kth smallest number is: " +
    str(find_Kth_smallest([[2, 6, 8], [3], [1, 3, 4]], 5)))
# Result expect = 4
