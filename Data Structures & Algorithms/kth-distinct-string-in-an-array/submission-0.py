class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}

        for s in arr:
            if s not in d:
                d[s] = 0
            d[s] += 1


        values = []

        for key, v in d.items():
            if v == 1:
                values.append(key)

        return values[k - 1] if len(values) >= k else ""