class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)

        for n in nums:
            h[n] += 1

        rev = sorted(h.items(), key=lambda item : item[1], reverse=True)

        ans = []

        for i in range(len(rev)):
            ans.append(rev[i][0])

        return ans[:k]
        