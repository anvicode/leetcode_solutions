class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, curr, length = 0, 0, float("inf")
        for R, V in enumerate(nums):
            curr += V
            while curr >= target:
                length = min(R - L + 1, length)
                curr -= nums[L]
                L += 1
        return 0 if length == float("inf") else length
