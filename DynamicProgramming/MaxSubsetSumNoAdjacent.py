'''
Write a function that takes in an array of positive integers and returns the max sum of non-adjacent elements of the array
'''
# O(n) Time | O(n) Space
def max_subset_sum_no_adjacent(array):
    if not len(array):
        return 
    elif len(array) ==1:
        return array[0]

    #Base Cases
    max_sums = array[:]
    max_sums[1] = max(array[0], max_sums[1])

    for i in range(2,len(array)):
        max_sums[i] = max(max_sums[i-1], max_sums[i-2] + array[i] )
    return max_sums[-1]

# O(n) Time | O(1) Space
def max_subset_sum_no_adjacent_improved(array):
    if not len(array):
        return 
    elif len(array) ==1:
        return array[0]
    
    #Base Cases
    second = array[0]
    first = max(array[0], array[1])

    for i in range(2,len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first



#Test Case
print(max_subset_sum_no_adjacent([7,10,12,7,9,14]))
print(max_subset_sum_no_adjacent_improved([7,10,12,7,9,14]))
#Result = 33

