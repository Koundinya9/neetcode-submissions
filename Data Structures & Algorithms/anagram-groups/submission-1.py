class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            sorteds = ''.join(sorted(s))
            if sorteds not in h:
                h[sorteds] = [s]

            else:
                h[sorteds].append(s)

        return list(h.values())