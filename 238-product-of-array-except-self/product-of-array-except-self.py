class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[]

        preProduct = 1

        for i in range(len(nums)):
            preProduct *= nums[i]
            pre.append(preProduct)
        
        post=[]

        postProduct = 1

        for j in range(len(nums)-1,-1,-1):
            postProduct *= nums[j]
            post.append(postProduct) 

        post = post[::-1]

        for i in range(len(nums)):
            if i == 0:
                nums[i] = post[i+1]
            elif i == len(nums)-1:
                nums[i] = pre[i-1]
            else:
                nums[i] = pre[i-1]*post[i+1] 

        return nums 

        