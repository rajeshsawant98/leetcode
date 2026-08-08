class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def max_left_aligned(intervals):
            intervals.sort()
            j = 0
            total = 0
            answer = 0
            n = len(intervals)

            for i in range(n):
                j = max(j, i)

                start = intervals[i][0]
                window_end = start+k-1

                # interval completely fits within window
                while j<n and intervals[j][1]<= window_end:
                    left, right, value = intervals[j]
                    total += (right-left+1)*value
                    j+= 1

                current = total
                    
                # the last interval partially fits within window
                if j<n and intervals[j][0]<=window_end:
                    left, right, value = intervals[j]
                    overlap = window_end-left+1
                    current += overlap*value

                answer = max(answer, current)

                # slide the left interval
                if i<j:
                    left, right, value = intervals[i]
                    total -= (right-left+1)*value

            return answer

        answer = max_left_aligned(coins[:])

        mirrored = [[-right, -left, value] for left, right, value in coins]

        return max(answer, max_left_aligned(mirrored))