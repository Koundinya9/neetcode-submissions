class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []

        potions.sort()

        for i in range(len(spells)):
            l, r = 0, len(potions) - 1

            while l <= r:
                m = (l + r) // 2

                prod = potions[m] * spells[i]

                if prod >= success:
                    r = m - 1
                else:
                    l = m + 1
                
            ans.append(len(potions) - l)

        return ans