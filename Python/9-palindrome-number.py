class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xs = str(x)
        return True if xs == xs[::-1] else False

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        buff = x
        rn = 0
        while buff != 0:
            d = buff % 10
            rn = rn * 10 + d
            buff //= 10
        return rn == x
