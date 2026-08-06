class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        # count = 0
        # minHeap = costs
        # heapq.heapify(costs)
        # while coins > 0 and minHeap:
        #     if minHeap[0] <= coins:
        #         count += 1
        #         cost = heapq.heappop(minHeap)
        #         coins -= cost
        #     else:
        #         break
        
        # return count

        m = max(costs)
        icecreams = 0

        Count = [0] * (m + 1)

        for cost in costs:
            Count[cost] += 1

        for cost in range(1, m + 1) :

            if Count[cost] == 0:
                continue

            if coins < cost:
                break
            
            count = min(Count[cost], coins// cost)

            coins -= count * cost

            icecreams += count
        
        return icecreams





