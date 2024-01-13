class Solution:
    def romanToInt(self, s: str) -> int:
        ht = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and ht[s[i]] < ht[s[i + 1]]:
                res -= ht[s[i]]
            else:
                res += ht[s[i]]
        return res
