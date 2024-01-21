class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        hm = {}
        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = t[i]
            elif hm[s[i]] != t[i]:
                return False
        return True
