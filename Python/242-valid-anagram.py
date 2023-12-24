class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hts = {}
        htt = {}
        for i in s:
            if i in hts:
                hts[i] += 1
            else:
                hts[i] = 1
        for i in t:
            if i in htt:
                htt[i] += 1
            else:
                htt[i] = 1
        return hts == htt
