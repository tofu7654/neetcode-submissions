class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        dict1, dict2 = {}, {}
        for letter in s:
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] += 1
        
        for letter in t:
            if letter not in dict2:
                dict2[letter] = 1
            else:
                dict2[letter] += 1

        return dict1 == dict2