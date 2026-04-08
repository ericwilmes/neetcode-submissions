class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def palin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def ite(start, end, curr):
            if end >= len(s):
                if start == end:
                    # we last had a palindrome
                    output.append(curr)
                return
            
            if palin(start, end):
                # add to single part of output
                ite(end+1, end+1, curr + [s[start:end+1]])
            ite(start, end+1, curr)



        ite(0, 0, [])

        print(output)

        return output