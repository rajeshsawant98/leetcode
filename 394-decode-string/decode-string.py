class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for c in s:

            if c != "]":
                stack.append(c)
            
            else:

                substring = ""

                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                
                multiplier = ""

                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                
                stack.append(int(multiplier) * substring)
        

        return "".join(stack)
                

