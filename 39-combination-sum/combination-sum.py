class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(candidates)

        def backtrack(i,sol,total):
            if total == target:
                res.append(sol[:])
                return
            
            if i == n or total > target:
                return
            
            sol.append(candidates[i])
            backtrack(i,sol,total+candidates[i])

            sol.pop()
            backtrack(i+1,sol,total)

            return
        
        backtrack(0,[],0)

        return res