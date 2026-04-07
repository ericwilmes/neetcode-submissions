class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = [[]]
        output = []

        for num in nums:
            for s in subsets:
                new_num = sum(s) + num
                if new_num > target:
                    continue
                elif sum(s) + num == target:
                    # add to output
                    output.append(s + [num])
                else:
                    # recurse
                    subsets.append(s + [num])

        return output