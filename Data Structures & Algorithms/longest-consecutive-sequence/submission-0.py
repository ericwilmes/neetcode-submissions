class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_num = 0
        for num in num_set:
            if num-1 in num_set:
                continue
            
            curr_num = num
            while curr_num in num_set:
                curr_num += 1
            max_num = max(curr_num - num, max_num)

        return max_num