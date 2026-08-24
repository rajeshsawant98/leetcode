class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        lenRes = 0

        for i in range(len(s)):

            #even substrings
            l = i 
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    sublen = r - l + 1
                    if sublen > lenRes:
                        lenRes = sublen
                        res = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break

            #odd substrings
            l=r= i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    sublen = r - l + 1
                    if sublen > lenRes:
                        lenRes = sublen
                        res = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
        
        return res