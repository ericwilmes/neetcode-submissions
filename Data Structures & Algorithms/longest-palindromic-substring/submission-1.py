class Solution:
    def longestPalindrome(self, s: str) -> str:
        # either add char to string or skip to next
        output = ""
        outLen = 0

        for i in range(len(s)):
            # odd
            # if palindrome centered at i
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > outLen:
                    output = s[l:r+1]
                    outLen = r - l + 1
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > outLen:
                    output = s[l:r+1]
                    outLen = r - l + 1
                l -= 1
                r += 1
            
                

        return output