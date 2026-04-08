class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in parentheses and len(stack) > 0:
                last = stack.pop()
                if last != parentheses[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0