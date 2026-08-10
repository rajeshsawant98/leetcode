class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        rankMap = defaultdict(list)

        for i,n in enumerate(arr):
            rankMap[n].append(i)

        res=[0] * len(arr)

        arr.sort()
 
        rank=1

        for i in range(len(arr)):

            if i> 0 and arr[i] > arr[i-1]:
                rank +=1
            
            for idx in rankMap[arr[i]]:
                res[idx] = rank
            
            

        return res