class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique={}

        for i in nums:
            if i not in unique:
                unique[i]=1
            else:
                return True
        
        return False
        