class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]

        i = 0
        j = 0
        k = 0

        while i < m + n:
            if k >= m:
                nums1[i] = nums2[j]
                j += 1
            elif j >= n:
                nums1[i] = temp[k]
                k += 1
            elif nums2[j] <= temp[k]:
                nums1[i] = nums2[j]
                j += 1
            else:
                nums1[i] = temp[k]
                k += 1
            i += 1