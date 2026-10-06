class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s)!=len(t):
            return False
        for i in s:
            d[i] = 1+d.get(i, 0)

        for i in t:
            if i not in d:
                return False
            elif d.get(i)!=t.count(i):
                return False
        return True