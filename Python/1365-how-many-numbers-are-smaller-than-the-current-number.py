class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, v in enumerate(nums):
            for j, val in enumerate(nums):
                if i != j and val < v:
                    res[i] += 1
        return res
