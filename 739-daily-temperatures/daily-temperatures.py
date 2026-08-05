class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] #would contain temp and index 

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                topTemp, topIndex = stack.pop()
                res[topIndex] = i - topIndex
            stack.append([t,i])
        
        return res