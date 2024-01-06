class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for i in strs:
            si = "".join(sorted(i))
            if si not in ht:
                ht[si] = [i]
            else:
                ht[si].append(i)
        return [i for i in ht.values()]
