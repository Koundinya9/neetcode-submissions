class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)
        mx = ans[-1]

        for i in range(len(arr) - 2, -1, -1):
            if arr[i + 1] > mx:
                mx = arr[i + 1]
            ans[i] = mx

        return ans
        