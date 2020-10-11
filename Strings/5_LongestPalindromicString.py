class Solution(object):
    
    #Time O(n^2) where n is the length of the string
    #Space O(1)
    def longest_palindrome(self, string):
        if len(string) <= 1:
            return string
        current_longest = [0,1]
        for i in range(1,len(string)):
            #if palindrome length is odd
            odd = self.get_longest_palindrome(string, i-1, i+1 )
            #if palindrome length is even
            even = self.get_longest_palindrome(string, i, i-1 )
            longest = max(odd, even, key= lambda x:x[1] - x[0])
            current_longest = max(longest, current_longest, key= lambda x:x[1] - x[0])
        return string[current_longest[0]:current_longest[1]]
    
    def get_longest_palindrome(self, string, left_index, right_index ):
        while left_index>=0 and right_index < len(string):
            if string[left_index] != string[right_index]:
                break
            left_index -=1
            right_index+=1
        return [left_index+1, right_index]

#Test Case
print(Solution().longest_palindrome("abaxyzzyxf"))


