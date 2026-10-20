class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        cache = {}
        
        def rec(i, flag):
            if flag:
                if i >= n:
                    return 0
                
            else:
                if i >= n - 1:
                    return 0

            if (i, flag) in cache:
                return cache[(i, flag)]

            cache[(i, flag)] = max(rec(i + 1, flag), nums[i] + rec(i + 2, flag))
            return cache[(i, flag)]


        return max(rec(0, False), rec(1, True))
        