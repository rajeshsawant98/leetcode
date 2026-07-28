class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0] + nums[1] + nums[2] 
        minDelta = abs(res - target)

        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, len(nums) - 1

            while(l < r):
                Total = nums[i] + nums[l] + nums[r] 

                delta = abs(Total - target)
                if delta < minDelta:
                    minDelta = delta
                    res = Total

                if Total == target:
                    return Total
                if Total > target:
                    r -=1
                else:
                    l +=1

                    
        
        return res