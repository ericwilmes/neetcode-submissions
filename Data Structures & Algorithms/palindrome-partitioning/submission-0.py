class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def palin(st):
            l = 0
            r = len(st) - 1
            while l < r:
                if st[l] != st[r]:
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
            sub_s = s[start:end+1]
            
            if palin(sub_s):
                # add to single part of output
                ite(end+1, end+1, curr + [sub_s])
            ite(start, end+1, curr)



        ite(0, 0, [])

        print(output)

        return output