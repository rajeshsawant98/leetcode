class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        inSum = sum(nums[:k])  
        maxSum = inSum    

        l, r = 0, k
        while r < len(nums):
            inSum = inSum - nums[l] + nums[r]
            maxSum = max(maxSum, inSum)
            l += 1
            r += 1

        return maxSum/float(k)
                
            