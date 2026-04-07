class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        inp = sorted(candidates)

        def it(i, curr, total):
            if i == len(inp):
                return
            val = inp[i]
            new_total = val + total

            if new_total == target:
                output.append(curr + [val])
                return
            elif new_total > target or i == len(inp):
                return

            it(i+1, curr + [val], new_total)

            while i != len(inp) and inp[i] == val:
                i += 1
            it(i, curr, total)

        it(0, [], 0)

        return output