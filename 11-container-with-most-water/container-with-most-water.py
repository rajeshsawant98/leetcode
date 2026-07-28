class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        l,r = 0,len(height) - 1

        while(l<r):

            minHeight = min(height[l],height[r])
            width = r - l

            maxArea= max(minHeight*width , maxArea)

            if height[l] > height[r]:
                r -=1
            else:
                l +=1
        
        return maxArea

