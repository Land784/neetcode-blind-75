from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(',']':'[','}':'{'}
        stack = deque()
        for char in s:
            if char in brackets:
                if not stack:
                    return False
                if brackets[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        
        return not stack

        