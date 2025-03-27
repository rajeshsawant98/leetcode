class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        carry= False
        l=len(digits)-1

        if(digits[l]==9):
                digits[l]=0
                carry = True
        else:
                digits[l] +=1
                return digits

        for i in range(l-1,-1,-1):
            if carry :
                digits[i] += 1
                if digits[i]==10:
                    digits[i]=0
                else:
                    carry = False
           
        
        if carry :
            return [1] + digits
        else:
            return digits


