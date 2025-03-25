class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=0

        cmap={}
        m=0

        while(r<len(s)):
            if s[r] in cmap:
                l = max(cmap[s[r]] + 1, l)
            cmap[s[r]]=r
            m = max(m,r-l+1)
            r+=1
        
        return m
