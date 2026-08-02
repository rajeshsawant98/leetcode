from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = collections.deque()

        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while q and fresh>0:

            for _ in range(len(q)):
                row, col = q.popleft()

                for dr,dc in directions:
                    r,c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))
                    
                
            
            minutes +=1
        
        return minutes if fresh <= 0 else -1