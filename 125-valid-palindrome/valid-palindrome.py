class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i,j= 0, len(s)-1
        while(i<=j):
            if not (s[i].isalpha() or s[i].isdigit()):
                i +=1
                continue
            if not (s[j].isalpha() or s[j].isdigit()):
                j -=1
                continue
            elif(s[i].lower()==s[j].lower()):
                i +=1
                j -=1
            else:
                return False

        return True