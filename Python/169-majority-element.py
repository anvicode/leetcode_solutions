class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ht = {}
        for i in nums:
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1
        for i in ht:
            if ht[i] > n / 2:
                return i
