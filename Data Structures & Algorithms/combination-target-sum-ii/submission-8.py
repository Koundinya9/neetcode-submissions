class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(path, i, sm):

            if sm == target:
                ans.append(path[:])
                return
            
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                if sm + candidates[idx] > target:
                    return


                path.append(candidates[idx])
                backtrack(path, idx + 1, sm + candidates[idx])
                path.pop()

        candidates.sort()
        ans = []
        backtrack([], 0, 0)
        return ans
        