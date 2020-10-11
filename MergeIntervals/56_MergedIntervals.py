class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <2:
            return intervals
        
        #Sort 
        intervals.sort(key= lambda x: x[0])
        
        merged_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            if current_interval[0] <= end:
                end = max(current_interval[1], end)
            else:
                merged_intervals.append([start, end])
                start = current_interval[0]
                end = current_interval[1]
                
        merged_intervals.append([start,end])
        return merged_intervals

# Test Case
print("Merged intervals: ", end='')
print(Solution().merge([[1,4],[4,5]]))
print()
print("Merged intervals: ", end='')
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print()