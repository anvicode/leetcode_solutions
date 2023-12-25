class Solution:
    def isPalindrome(self, s: str) -> bool:
        conv_str = "".join(filter(str.isalnum, s)).lower()
        return True if conv_str == conv_str[::-1] else False
