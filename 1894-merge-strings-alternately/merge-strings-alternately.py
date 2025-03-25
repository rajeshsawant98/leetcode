class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        ans=""

        p1=0
        p2=0
        l1= len(word1)
        l2= len(word2)

        while (p1< l1) and (p2<l2):
            ans += word1[p1]
            p1+=1
            ans += word2[p2]
            p2+=1
        
        if (l1-p1) != 0:
            ans = ans + word1[p1:l1]
        elif (l2-p2) != 0:
            ans = ans + word2[p2:l2]
        
        return ans

        