class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l,r=0,len(nums)-1
        
        for i in range(len(nums)):
            m= l+ (r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]< target:
                l= m+1
            elif nums[m] > target:
                r= m-1
        
        return -1
            