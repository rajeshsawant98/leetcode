class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        count = 0
        minHeap = costs
        heapq.heapify(costs)
        while coins > 0 and minHeap:
            if minHeap[0] <= coins:
                count += 1
                cost = heapq.heappop(minHeap)
                coins -= cost
            else:
                break
        
        return count



