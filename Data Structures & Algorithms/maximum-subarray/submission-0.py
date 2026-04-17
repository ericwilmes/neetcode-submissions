class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxv = nums[0]
        cum_sum = 0
        for num in nums:
            if cum_sum < 0:
                cum_sum = 0
            cum_sum += num
            maxv = max(maxv, cum_sum)

        return maxv