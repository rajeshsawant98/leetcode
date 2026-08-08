class Solution:
    def reorganizeString(self, s: str) -> str:
        
        FMap = {}
        Length = len(s)
        for c in s:
            FMap[c] = 1 + FMap.get(c, 0)
        
        maxHeap = [ [-count, c] for c, count in FMap.items()]
        heapq.heapify(maxHeap)

        output = ""
        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            

            # most frequest except for the prev 
            cnt, char = heapq.heappop(maxHeap)
            output += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]
            
        
        return output






            