class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i in nums:
            arr[i - 1] += 1
        res = [i + 1 for i, v in enumerate(arr) if v == 0]
        return res
