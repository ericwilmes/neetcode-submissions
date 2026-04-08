class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                output.append(subset)
                return
            # if not subset:
            #     return []

            print(nums, i)
            num = nums[i]

            # add curr item
            backtrack(i+1, subset + [num])

            # don't add curr item
            while i < len(nums) and nums[i] == num:
                i += 1
            backtrack(i, subset)


        backtrack(0, [])

        return output