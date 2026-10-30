class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = [0]

        def rec(i, level):
            if i >= len(nums):
                if level:
                    temp = 0
                    for n in level:
                        temp ^= n
                    ans[0] += temp
                return

            level.append(nums[i])
            rec(i + 1, level)
            level.pop()
            rec(i + 1, level)

            return

        rec(0, [])
        return ans[0]



            
