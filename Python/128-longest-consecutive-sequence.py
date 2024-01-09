class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in ns:
                nxt = 0
                while i + nxt in ns:
                    nxt += 1
                res = max(nxt, res)
        return res
