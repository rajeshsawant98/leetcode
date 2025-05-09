class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l,r=0,len(nums)-1

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]
            