class Solution:
    def isHappy(self, n: int) -> bool:
        hs = set()
        while n != 1:
            if n in hs:
                return False
            hs.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return True
