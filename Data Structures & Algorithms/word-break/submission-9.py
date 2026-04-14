class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def trav(l, r):
            if r > len(s):
                return not s[l:r+1]
            print(l, r, memo)
            if memo.get(r, False):
                return memo[r]
            subs = s[l:r+1]
            print(subs)
            if subs in wordSet:
                memo[r] = True
                return trav(r+1, r+1) or trav(l, r+1)
            memo[r] = memo.get(r) or False
            return trav(l, r+1)

        trav(0, 0)
        print(memo)
        return memo[len(s)-1]