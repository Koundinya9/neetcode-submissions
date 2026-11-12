class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        d = {}

        for num in nums1:
            d[num[0]] = num[1]

        for num in nums2:
            if num[0] in d:
                d[num[0]] += num[1]
            else:
                d[num[0]] = num[1]

        ans = []
        for k, v in d.items():
            ans.append([k, v])

        ans = sorted(ans, key = lambda x : x[0])
        return ans