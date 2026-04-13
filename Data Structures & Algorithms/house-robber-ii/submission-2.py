class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        one, two = 0, 0
        output = nums[0]

        for i in range(len(nums)-1):
            # first to end - 1
            num = nums[i]
            one, two = two, max(one + num, two)

        output = max(output, one, two)

        one, two = 0, 0
        for i in range(1, len(nums)):
            # second to end
            num = nums[i]
            one, two = two, max(one + num, two)

        output = max(output, one, two)
        return output