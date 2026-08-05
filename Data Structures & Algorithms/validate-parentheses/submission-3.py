class Solution:
    def isValid(self, s: str) -> bool:
        opened = set("({[")

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for ch in s:
            if ch in opened:
                stack.append(ch)
            else:
                if not stack or (stack.pop() != pairs[ch]):
                    return False
        
        return not stack