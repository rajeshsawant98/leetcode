class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        map ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        

        ans=0
        prev=0

        for c in reversed(s):
            value = map[c]
            if value < prev:
                ans -= value
            else:
                ans += value
                prev = value

        return ans
            