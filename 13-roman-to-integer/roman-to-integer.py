class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        map ={}
        map["I"]= 1
        map["V"]= 5
        map["X"]= 10
        map["L"]=50
        map["C"]=100
        map["D"]=500
        map["M"]=1000

        ans=0
        prev=0

        for c in reversed(s):
            value = map[c]
            if value < prev:
                ans -= value
            if value >= prev:
                ans += value
                prev = value
        return ans
            