class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        Baskets = {}
        maxFruits = 0

        l= 0

        for r in range(len(fruits)):

            Baskets[fruits[r]] = 1 + Baskets.get(fruits[r],0)

            while len(Baskets) > 2:

                Baskets[fruits[l]] -= 1

                if Baskets[fruits[l]] == 0:
                    del Baskets[fruits[l]]
                
                l += 1
            
            maxFruits = max(maxFruits, r - l + 1)
        

        return maxFruits


                
            
