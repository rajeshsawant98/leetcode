from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)!= len(t): 
            return False


        Cs ={}
        Ct ={}

        for i in range(len(s)):
            Cs[s[i]]= Cs.get(s[i],0)+1
            Ct[t[i]]= Ct.get(t[i],0)+1
        
        return Cs == Ct