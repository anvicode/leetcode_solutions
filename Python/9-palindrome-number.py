class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xs = str(x)
        return True if xs == xs[::-1] else False
