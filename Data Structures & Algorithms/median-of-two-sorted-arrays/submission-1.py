class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        comb = nums1 + nums2

        comb.sort()

        n = len(comb)

        if n % 2 == 0:
            r = n // 2
            l = r - 1
            return float(comb[l] + comb[r]) / 2
        else:
            m = n // 2
            return comb[m]
        

        