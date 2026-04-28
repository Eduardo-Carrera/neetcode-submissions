class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        count = 0

        for operation in logs:
            if operation == "../" and count > 0:
                count -= 1
            elif operation != "./" and operation != "../":
                count += 1
        
        return count