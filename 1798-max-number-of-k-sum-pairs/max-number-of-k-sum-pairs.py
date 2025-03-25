class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums:
            return 0

        nums.sort()

        L=0 
        R=len(nums)-1

        c=0

        while(L<R):
            sum = nums[L]+ nums[R]
            if sum == k:
                c +=1
                R -=1
                L +=1
            elif sum > k:
                R -=1
            else:
                L +=1
        
        return c



        