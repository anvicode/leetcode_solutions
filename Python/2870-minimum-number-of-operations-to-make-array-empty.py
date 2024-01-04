class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ht = {}
        c = 0
        for i in nums:
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1
        for i in ht:
            if ht[i] == 1:
                return -1
            c += ceil(ht[i] / 3)
        return c
