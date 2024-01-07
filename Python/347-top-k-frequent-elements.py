from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        res = []
        for _ in range(k):
            mv = max(c.values())
            mi = next(k for k, v in c.items() if v == mv)
            res.append(mi)
            del c[mi]
        return res
