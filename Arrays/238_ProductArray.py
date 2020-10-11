class Solution(object):
    #O(N) time | O(N) Space for left and right
    def product_except_self(self, nums):
        left = [0] * len(nums)
        right = [0] * len(nums)
        length = len(nums)
        product = [0] * len(nums)
        left[0] = 1
        right[length - 1] = 1
        

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for i in reversed(range(length-1)):
            right[i] = right[i+1] * nums[i+1]

        for i in range(length):            
            product[i] = right[i] * left[i]

        return product

    #O(N) time | O(1) Space as output does not count as extra space
    def product_except_self_optimum_space(self, nums):        
        length = len(nums)
        product = [0] * len(nums)
        product[0] = 1

        for i in range(1, len(nums)):
            product[i] = product[i-1] * nums[i-1]        
        
        right = 1
        for i in reversed(range(length)):
            product[i] = product[i] * right
            right *= nums[i]

        return product

#Test Case
nums = [1,2,3,4]
print(Solution().product_except_self(nums))
print(Solution().product_except_self_optimum_space(nums))
#Result: [24,12,8,6]