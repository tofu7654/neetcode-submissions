class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:

            # first check that both are alphanum and in bounds
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1

            # once validated, make lower and compare
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1

        return True

    def isAlphaNum(self, c: str) -> bool:
        return (
               ord("a") <= ord(c) <= ord("z") or
               ord("A") <= ord(c) <= ord("Z") or 
               ord("0") <= ord(c) <= ord("9")
               )
        