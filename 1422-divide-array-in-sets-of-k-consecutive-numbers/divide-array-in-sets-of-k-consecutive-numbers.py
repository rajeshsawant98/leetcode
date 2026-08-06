class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        Count = {}

        for n in nums:
            Count[n] = 1 + Count.get(n,0)

        
        minHeap = list(Count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            for i in range(start,start+k):
                if i not in Count:
                    return False
                
                Count[i] -= 1
                if Count[i] == 0:
                    if i != minHeap[0]:
                        return False 
                    heapq.heappop(minHeap)
        
        return True