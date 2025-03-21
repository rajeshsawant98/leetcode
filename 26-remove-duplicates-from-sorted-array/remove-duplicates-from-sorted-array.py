class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums1 =[]
        nmap={}
        k=0
        for i,n in enumerate(nums):
            if n not in nmap:
                nums1.append(n)
                nmap[n]=1
                k +=1
                
            
        nums[:]=nums1
        return k 
        
                
            