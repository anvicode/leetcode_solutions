class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x * x, nums))

    def sortedSquares3(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]
            if left > right:
                res.append(left)
                l += 1
            else:
                res.append(right)
                r -= 1
        res.reverse()
        return res
