class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        inter = s1.intersection(s2)
        s1 = s1 - inter
        s2 = s2 - inter
        return [list(s1), list(s2)]
