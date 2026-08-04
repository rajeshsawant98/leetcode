class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda i:i[0])

        minHeap = []

        for i in intervals:
            if minHeap and minHeap[0] <= i[0]:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, i[1])
        
        return len(minHeap)