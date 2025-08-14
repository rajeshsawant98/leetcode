class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        arr =["999","888","777","666","555","444","333","222","111","000"]

        for n in arr:
            if n in num:
                return n
        
        return ""
        