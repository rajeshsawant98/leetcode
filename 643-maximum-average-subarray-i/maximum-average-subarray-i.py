class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        inSum = sum(nums[:k])  
        maxAvg = inSum / float(k)     

        l, r = 0, k
        while r < len(nums):
            inSum = inSum - nums[l] + nums[r]
            maxAvg = max(maxAvg, inSum / float(k))
            l += 1
            r += 1

        return maxAvg
                
            