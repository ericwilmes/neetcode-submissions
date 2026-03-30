class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_helper(nums, target, 0, len(nums)-1)


    def search_helper(self, nums: list[int], target: int, l, r) -> int:
        if l > r:
            return -1
        m = (r + l) // 2
        
        if nums[m] < target:
            return self.search_helper(nums, target, m+1, r)
        if nums[m] > target:
            return self.search_helper(nums, target, l, m-1)
        return m
