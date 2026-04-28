class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == "+":
                if len(stack) > 1:
                    first = stack.pop()
                    second = stack.pop()
                    result = first + second
                    stack.append(second)
                    stack.append(first)
                    stack.append(result)
                    continue

            elif i == "C":
                if stack:
                    stack.pop()

            elif i == "D":
                if stack:
                    result = stack[-1] * 2
                    stack.append(result)
                    continue

            else:
                stack.append(int(i))

        result = 0        
        while stack:
            result += stack.pop()

        return result
            

