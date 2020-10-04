'''
Given an N * NN∗N matrix where each row and column is sorted in ascending order, 
find the Kth smallest element in the matrix.
Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
'''

from heapq import *

# O(K*logM) Time where M is total of input arrays
# O(M) Space
def find_Kth_smallest(matrix, k):
    min_heap = []

    #Push the first element of each row
    #We dont need to push more than K elements    
    for row in range(len(matrix)):
        heappush(min_heap, (matrix[row][0], 0, matrix[row]))

    #Take the smallest element in heap. If the running count is equal to k, return the number
    #if the row of the top element has more elements, add the next element to the heap
    count, value = 0,0

    while min_heap:
        value, col, current_row = heappop(min_heap)
        count +=1

        if count == k:
            break

        if len(current_row) > col + 1:
            heappush(min_heap, (current_row[col+1], col+1, current_row))
    return value

# Test Case
print("Kth smallest number is: " +
    str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))
#Result - 7

