class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visit =set()
        res= 0

        def bfs(r,c):
            
            q = collections.deque()

            q.append((r,c))
            visit.add((r, c))

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while q:
                row,col = q.popleft()

                for dr,dc in directions:
                    r,c = row+dr,col+dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
        



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    res += 1
                    bfs(r,c)
        

        return res
