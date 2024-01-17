class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > m:
                buff = m
                m = arr[i]
                arr[i] = buff
            else:
                arr[i] = m
        arr[-1] = -1
        return arr
