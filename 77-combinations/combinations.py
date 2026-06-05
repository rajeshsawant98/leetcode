class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res =[]
        
        def dfs(i,path):

            if len(path) == k:
                res.append(path[:])
                return 
            
            if i == n+1:
                return
            
            path.append(i)
            dfs(i+1,path)
            path.pop()
            dfs(i+1,path)

        dfs(1,[])

        return res