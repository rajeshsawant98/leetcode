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
            count = [0]*26 # to count the occurence of each chara in the string
            for c in s: # 
                count[ord(c) - ord("a")] += 1 
            res[tuple(count)].append(s)
        
        return list(res.values())

        # O(n.k)
        # O(n.k)

            