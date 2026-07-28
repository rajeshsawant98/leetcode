class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1,2,3,4...,100...,200

        numSet = set(nums) #o(n)
        longest = 0

        for n in numSet: 
            #check if it's a start of a subsequence

            if (n-1) not in numSet: #O(1) -> 
                length = 0 
                while (n+length) in numSet:
                    length += 1
                longest = max(length,longest)
        
        return longest
