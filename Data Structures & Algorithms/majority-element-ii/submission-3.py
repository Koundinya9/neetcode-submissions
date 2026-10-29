class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        threshold = len(nums) / 3

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

            ans = []
        for n, count in counts.items():
            if count > threshold:
                ans.append(n)

        return ans