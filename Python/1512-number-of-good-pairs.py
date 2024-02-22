class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        res = 0
        for n in nums_count:
            res += nums_count[n] * (nums_count[n] - 1) // 2
        return res
