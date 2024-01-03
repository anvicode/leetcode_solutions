class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        res = 0
        for s in bank:
            curr = 0
            for n in s:
                if n == "1":
                    curr += 1
            if curr > 0:
                res += prev * curr
                prev = curr
        return res
