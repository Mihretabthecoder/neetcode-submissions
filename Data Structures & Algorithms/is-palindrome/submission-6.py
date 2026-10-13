class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        alp = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        for i in s:
            if i in alp:
                ss += i.lower()

        n = ((len(ss))//2)
        for i in range(n):
            if ss[i]!= ss[len(ss)-(i+1)]:
                return False
        return True
