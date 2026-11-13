class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        res1 = {}
        res2 = {}

        for c in s:
            if c in res1:
                res1[c] += 1
            else:
                res1[c] = 1

        for c in t:
            if c in res2:
                res2[c] += 1
            else:
                res2[c] = 1

        for key in res1:
            if not key in res2:
                return False
            elif res2[key] != res1[key]:
                return False

        for key in res2:
            if not key in res1:
                return False

        return True
