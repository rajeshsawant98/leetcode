from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                qlen = len(q)

                directions = [(0,1),(1,0),(0,-1),(-1,0)]

                for _ in range(qlen):
                    row,col = q.popleft()

                    for dr,dc in directions:
                        r,c = row + dr , col + dc

                        if r >= 0 and r < rows and c >= 0 and c < cols and (r,c) not in visit and grid[r][c] == "1" :
                            q.append((r,c))
                            visit.add((r,c))
                    



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands +=1
                else:
                    continue

        
        return islands
        
