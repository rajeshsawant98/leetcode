class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # #brute sort all the strings and group the same ones that would take n*nlogn 

        # res = defaultdict(list)

        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        
        # return list(res.values())

        res = defaultdict(list)

        for s in strs:  # n 
            Count = [0] * 26 
            for c in s:  # k
                Count[ord(c) - ord("a")] += 1
            res[tuple(Count)].append(s)
        return list(res.values())

            