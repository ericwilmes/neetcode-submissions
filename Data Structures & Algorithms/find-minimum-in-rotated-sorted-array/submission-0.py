class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        m = (len(nums)-1) // 2
        left = nums[:m]
        right = nums[m:]

        min_left = self.findMin(left)
        min_right = self.findMin(right)

        return min_left if min_left < min_right else min_right