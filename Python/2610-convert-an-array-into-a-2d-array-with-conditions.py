from collections import defaultdict


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = defaultdict(int)

        for i in nums:
            r = d[i]
            if len(res) == r:
                res.append([])
            res[r].append(i)
            d[i] += 1

        return res
