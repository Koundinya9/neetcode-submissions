class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1


        i, j = 0, 1
        ans = 1
        if arr[j] > arr[i]:
            bigger = True
        else:
            bigger = False
        while j < len(arr):
            if arr[j] == arr[j - 1]:
                i = j
            else:
                if not bigger:
                    if arr[j] > arr[j - 1]:
                        bigger = True
                    else:
                        i = j - 1
                else:
                    if arr[j] < arr[j - 1]:
                        bigger = False
                    else:
                        i = j - 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans


            