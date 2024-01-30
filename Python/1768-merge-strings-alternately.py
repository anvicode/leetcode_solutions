class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        lw1, lw2 = len(word1), len(word2)
        res = ""
        while p1 < lw1 or p2 < lw2:
            if p1 < lw1:
                res += word1[p1]
                p1 += 1
            if p2 < lw2:
                res += word2[p2]
                p2 += 1
        return res
