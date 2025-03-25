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

        # cmap = {}
        # c = 0

        # for i in nums:
        #     cmap[i] = cmap.get(i, 0) + 1

        # for n in nums:
        #     diff = k - n
        #     if n == diff:
        #         if cmap.get(n, 0) >= 2:
        #             c += 1
        #             cmap[n] -= 2
        #             if cmap[n] <= 0:
        #                 cmap.pop(n)
        #     elif cmap.get(n, 0) > 0 and cmap.get(diff, 0) > 0:
        #         c += 1
        #         cmap[n] -= 1
        #         cmap[diff] -= 1
        #         if cmap[n] == 0:
        #             cmap.pop(n)
        #         if cmap[diff] == 0:
        #             cmap.pop(diff)

        # return c

        



        