class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i:i[0])


        res = [intervals[0]]

        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):

            start,end = intervals[i]

            if start > prevEnd:
                res.append([start,end])
            else:
                res[-1][1] = max(end,prevEnd)
            
            prevEnd = res[-1][1]
        
        return res

        

