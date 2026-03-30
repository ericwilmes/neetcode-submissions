class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums[:-1]):
            for j, next_num in enumerate(nums[i+1:]):
                if num + next_num == target:
                    new_j = j + i + 1
                    return [i, new_j]