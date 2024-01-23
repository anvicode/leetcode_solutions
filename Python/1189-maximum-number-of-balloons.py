class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ct = Counter(text)
        sample = Counter("balloon")
        res = len(text)
        for i in sample:
            res = min(res, ct[i] // sample[i])
        return res
