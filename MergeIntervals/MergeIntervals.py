'''
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # Sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1,len(intervals)):
        current_interval = intervals[i]
        if current_interval.start <= end: # there is an overlap
            end = max(current_interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = current_interval.start
            end = current_interval.end

    merged_intervals.append(Interval(start, end))

    return merged_intervals
    
    


# Test Cases:
print("Merged intervals: ", end='')
for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
print()

print("Merged intervals: ", end='')
for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
print()

print("Merged intervals: ", end='')
for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
print()