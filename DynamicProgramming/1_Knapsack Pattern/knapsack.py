'''
Given two integer arrays to represent weights and profits of ‘N’ items, 
we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. 
Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
'''

'''
Algorithm: 
for each item 'i' 
  create a new set which INCLUDES item 'i' if the total weight does not exceed the capacity, and 
     recursively process the remaining capacity and items
  create a new set WITHOUT item 'i', and recursively process the remaining items 
return the set from the above two sets with higher profit 
'''

#Brute Foce Solution -- O(2^n) Time where n -> total number of items

def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, current_index):
    #Base Case
    if capacity <=0 or current_index >= len(profits):
        return 0
    
    #recursive call - after choosing the element at the current index
    #if the weight of the element at current index exceeds the capacity, we should not process 
    profit_with_element=0
    if weights[current_index] < capacity:
        profit_with_element = profits[current_index] + knapsack_recursive(profits, weights, capacity - weights[current_index], current_index + 1 )

    # recursive call after exclusing the element at the current index:
    profit_without_element = knapsack_recursive(profits, weights, capacity, current_index + 1)

    return max(profit_with_element, profit_without_element)

#Test Case
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

