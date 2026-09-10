class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c in hashMap:
                if not stack:
                    return False
                if stack.pop() != hashMap[c]:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
