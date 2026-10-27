class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        match1 = match2 = match0 = False

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            if t[0] == target[0]:
                match0 = True

            if t[1] == target[1]:
                match1 = True

            if t[2] == target[2]:
                match2 = True

            if match0 and match1 and match2:
                return True

            

        return False