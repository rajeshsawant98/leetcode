class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda i:i[1])

        count = 0

        prev = intervals[0][1]

        for start,end in intervals[1:]:
            if start < prev:
                count +=1
            else:
                prev = end
        
        return count