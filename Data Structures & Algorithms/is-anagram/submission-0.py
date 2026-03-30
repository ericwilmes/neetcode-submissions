class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}

        for letter in s:
            if letter in s_chars:
                s_chars[letter] += 1
            else:
                s_chars[letter] = 1

        for letter in t:
            if letter in t_chars:
                t_chars[letter] += 1
            else:
                t_chars[letter] = 1
        
        return s_chars == t_chars