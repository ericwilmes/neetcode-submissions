class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        r = 0
        substring = set()

        while r < len(s):
            if s[r] in substring:
                substring.remove(s[l])
                l += 1
            else:
                substring.add(s[r])
                r += 1
            max_len = max(max_len, r - l)

        return max_len