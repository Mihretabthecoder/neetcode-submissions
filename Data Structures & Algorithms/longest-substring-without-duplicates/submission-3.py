class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0
        d = set()
        longest = 0

        while r <= len(s)-1:
            if s[r] not in d:
                d.add(s[r])
                r+=1
                longest = max(longest, r-l)
            else:
                d.remove(s[l])
                l += 1
        return longest
        