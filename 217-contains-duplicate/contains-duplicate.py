class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hs = set()

        for i in range(len(nums)):
            if nums[i] in hs:
                return True
            else:
                hs.add(nums[i])
        
        return False