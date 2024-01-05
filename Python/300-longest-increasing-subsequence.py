class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and res[i] < res[j] + 1:
                    res[i] = res[j] + 1
        return max(res)
