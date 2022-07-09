class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}
        o = [v for k, v in brackets.items()]
        for char in s:
            if char in o:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                test = stack.pop()
                if test != brackets.get(char,0):
                    return False
        if len(stack) != 0:
            return False
        return True