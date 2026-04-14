class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxv, minv = 1, 1
        output = nums[0]

        for num in nums:
            new_max = num * maxv
            new_min = num * minv
            maxv = max(new_max, new_min, num)
            minv = min(new_max, new_min, num)

            output = max(maxv, output)

        return output
