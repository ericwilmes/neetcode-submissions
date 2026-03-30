class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, num in enumerate(nums):
            difference = target - num
            if num in differences:
                return [differences[num], i]
            differences[difference] = i