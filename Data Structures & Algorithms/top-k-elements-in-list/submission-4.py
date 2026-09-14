class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        ans = [] 

        rev = sorted(d.items(), key = lambda x : x[1], reverse=True)

        for i in range(len(rev)):
            ans.append(rev[i][0])

        return ans[:k]
        