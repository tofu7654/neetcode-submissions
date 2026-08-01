class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1, dictionary2 = {}, {}
        for letter in s:
            if letter in dictionary1:
                dictionary1[letter] += 1
            else:
                dictionary1[letter] = 1

        for letter in t:
            if letter in dictionary2:
                dictionary2[letter] += 1
            else:
                dictionary2[letter] = 1

        if dictionary1 == dictionary2:
            return True
        else:
            return False
