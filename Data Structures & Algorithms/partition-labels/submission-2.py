class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {}
        first = {}

        for i in range(len(s)):
            last[s[i]] = i

        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i

        ans = []
        start, end = 0, last[s[0]]
        for c, i in first.items():
            if i > end:
                ans.append(end - start + 1)
                start = i
                end = last[c]
            else:
                end = max(end, last[c])


        ans.append(end - start + 1)
        return ans