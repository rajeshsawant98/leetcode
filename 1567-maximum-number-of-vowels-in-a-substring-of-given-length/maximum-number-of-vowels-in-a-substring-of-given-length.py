class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = 0
        
        
        for i in range(0, k):
            if s[i] == 'a' or s[i]== 'e' or s[i]=='i' or s[i]=='o' or s[i]=='u' :
                count +=1
        
        maxCount = count

        if maxCount == k:
            return k
        
        l,r = 0,k

        while (r<len(s)):

            if s[l] == 'a' or s[l]== 'e' or s[l]=='i' or s[l]=='o' or s[l]=='u' :
                count -= 1
            
            if s[r] == 'a' or s[r]== 'e' or s[r]=='i' or s[r]=='o' or s[r]=='u' :
                count +=1
            
            maxCount = max(maxCount,count)
            l += 1
            r +=1 
        
        return maxCount
