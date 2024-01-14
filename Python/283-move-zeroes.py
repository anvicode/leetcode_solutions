class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        target = 0
        zeroes = []
        i = j = 0
        n = len(nums)
        while j < n:
            if nums[i] == target:
                zeroes.append(nums.pop(i))
            else:
                i += 1
            j += 1
        nums += zeroes
