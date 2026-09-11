class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            p=''.join(sorted(s))
            res[p].append(s)

        return list(res.values())
        