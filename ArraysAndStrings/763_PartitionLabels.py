from collections import defaultdict
class Solution():
    #O(N) Time | O(N) Space
    def partition_labels(self, s):
        partition_length = []
        char_last_map = defaultdict()
        #O(N) Time
        for i in range(len(s)):
            char_last_map[s[i]] = i
        print(char_last_map)
        start, left, right = 0,0,0
        
        #O(N) Time
        while left < len(s):
            last_seen = char_last_map[s[left]]
            
            if last_seen > right:
                right = last_seen            
            
            if left == right:
                partition_length.append(right - start + 1)
                start = left + 1
            left = left + 1
        return partition_length


#Test Case:
S = "ababcbacadefegdehijhklij"
print(Solution().partition_labels(S))
#Result: [9,7,8]