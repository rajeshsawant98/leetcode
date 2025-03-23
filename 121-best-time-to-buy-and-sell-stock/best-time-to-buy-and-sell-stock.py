class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit=0

        p1=0
        p2=1

        while( p2< len(prices)):
            if prices[p1]< prices[p2]:
                maxProfit = max(maxProfit , (prices[p2]-prices[p1]))
            else:
                p1=p2
            p2 +=1
        
        return maxProfit
