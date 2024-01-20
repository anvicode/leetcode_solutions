class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

    def lengthOfLastWord2(self, s: str) -> int:
        c = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if c > 0:
                    return c
            else:
                c += 1
        return c
