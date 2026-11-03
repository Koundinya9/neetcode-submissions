class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d = {}

        for i in range(len(nums2)):
            p = i + 1

            while p < len(nums2) and nums2[p] < nums2[i]:
                p += 1

            if p == len(nums2):
                d[nums2[i]] = -1
            
            else:
                d[nums2[i]] = nums2[p]

        ans = [0] * len(nums1)

        for i in range(len(nums1)):
            ans[i] = d[nums1[i]]

        return ans



