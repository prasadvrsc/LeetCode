'''
Implement a function that takes an array arr, a testVariable (containing the number to search) and currentIndex (containing the starting index) as parameters. 
This function should output the index of the first occurrence of testVariable in arr. 
If testVariable is not found in arr it should return -1−1.
'''

def first_index_iterative(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Test Case
arr = [9, 8, 1, 8, 1, 7]
target = 1
print(first_index_iterative(arr, target))