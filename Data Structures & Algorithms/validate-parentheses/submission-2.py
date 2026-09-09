class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    x = stack.pop()
                    if x == '(' and s[i] != ')':
                        return False
                    if x == '{' and s[i] != '}':
                        return False
                    if x == '[' and s[i] != ']':
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False