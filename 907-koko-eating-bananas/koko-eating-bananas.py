class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l,r = 1, max(piles)
        res=r

        while(l<=r):

            m=(l+r)//2
            hours=0
            
            for p in piles:
                hours += math.ceil(float(p)/m)
            
            if hours<=h:
                res= m
                r = m-1
            else:
                l= m+1
        
        return res



        