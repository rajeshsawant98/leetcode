class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)


        k = float("inf")

        while(l <= r):

            mid = (l + r)// 2
            hours = 0
            for p in piles:
                hours += ceil(p/mid)
            
            if hours <= h:
                k = min(mid, k)
                r = mid - 1
            else:
                l = mid + 1 
        
        return k
            