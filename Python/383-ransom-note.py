class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mm = {}

        for i in magazine:
            if i not in mm:
                mm[i] = 1
            else:
                mm[i] += 1

        for i in ransomNote:
            if i not in mm or mm[i] == 0:
                return False
            else:
                mm[i] -= 1
        return True
