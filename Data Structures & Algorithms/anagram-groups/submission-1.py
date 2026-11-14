class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26  # characters
            for c in s.lower():
                index = ord(c) - ord("a")
                count[index] += 1
            res[tuple(count)].append(s)
        return list(res.values())