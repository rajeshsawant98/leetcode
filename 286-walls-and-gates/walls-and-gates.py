from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])

        q= deque()
        visit = set()
        dist = 0 

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        

        def addCell(r,c):
            if r not in range(rows) or c not in range(cols) or rooms[r][c] == -1 or (r,c) in visit:
                return
            
            q.append((r,c))
            visit.add((r,c))

        
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist

                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            

            dist +=1