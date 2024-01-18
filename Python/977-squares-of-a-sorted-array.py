class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x * x, nums))
