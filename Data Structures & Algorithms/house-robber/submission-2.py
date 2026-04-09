class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        one, two = nums[0], max(nums[1], nums[0])

        for i in range(2, n):
            num = nums[i]
            
            one, two = two, max(num+one, two)

        return max(one, two)