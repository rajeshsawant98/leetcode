class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        

        Set1= set(nums1)
        Set2= set(nums2)

        # for n in nums1:
        #     if  n not in Set1:
        #         Set1.add(n)
        
        # for m in nums2:
        #     if m not in Set2:
        #         Set2.add(m)
        
        return [list(Set1 - Set2) , list(Set2-Set1)]
