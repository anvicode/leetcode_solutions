class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, v in enumerate(nums):
            total_sum -= v
            if left_sum == total_sum:
                return i
            left_sum += v
        return -1
