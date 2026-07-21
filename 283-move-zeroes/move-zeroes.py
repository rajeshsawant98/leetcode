class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nextNonZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
                nextNonZero +=1
