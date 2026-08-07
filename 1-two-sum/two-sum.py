class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        valueMap = {}

        for i,n in enumerate(nums):

            diff = target - n 
            if diff in valueMap:
                return [valueMap[diff],i]
            
            valueMap[n] = i
        
    