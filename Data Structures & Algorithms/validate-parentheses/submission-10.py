class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            stack.append(bracket)
            if bracket == ")" or bracket == "}" or bracket == "]":
                if len(stack) > 1:
                    if stack[-1] == ")" and stack[-2] == "(" or stack[-1] == "}" and stack[-2] == "{" or stack[-1] == "]" and stack[-2] == "[":
                        stack.pop()
                        stack.pop()
                    else:
                        return False
            

        if len(stack) > 0:
            return False
        else:
            return True
