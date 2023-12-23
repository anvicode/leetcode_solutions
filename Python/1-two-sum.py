class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for j, vv in enumerate(nums):
                if i != j and v + vv == target:
                    return [i, j]
