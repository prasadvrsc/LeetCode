'''
Given an array of intervals representing ‘N’ appointments, 
find out if a person can attend all the appointments.
Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
'''

#O(nlogn) Time
class Solution(object):
    def can_attend_all_appointments(self,intervals):
        if len(intervals) < 2:
            return True
        intervals.sort(key = lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            current_interval = intervals[i]
            next_interval = intervals[i+1]
            if (current_interval[1] > next_interval[0] ):
                return False
            i += 1
        return True

#Test Cases
print("Can attend : " + 
        str(Solution().can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
print("Can attend : " + 
        str(Solution().can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
print("Can attend : " + 
        str(Solution().can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))








