class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # stack =[]
        # ClosedBracMap = { ']': '[','}':'{',')':'('}

        # for c in s:
        #     if c in ClosedBracMap: 
        #         if stack and stack[-1]==ClosedBracMap[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
            
        # return True if not stack else False
                
            
        
        stack =[]

        for c in s:
            if c == ')' or c == ']' or c == '}': 
                if stack:
                    if c== ')' and stack[-1]=='(':
                        stack.pop()
                    elif c== ']' and stack[-1]=='[':
                        stack.pop()
                    elif c== '}' and stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False


