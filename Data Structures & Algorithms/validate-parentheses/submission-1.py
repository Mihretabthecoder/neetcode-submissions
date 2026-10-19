class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char = {")" : "(", "}" : "{", "]" : "["}

        for i in s:
            if i in char:
                if stack and stack[-1] == char[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
        