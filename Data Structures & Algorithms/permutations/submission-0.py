class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            new_out = []
            for item in output:
                for i in range(len(item)+1):
                    new_item = item[:]
                    new_item.insert(i, num)
                    new_out.append(new_item)
            output = new_out

        return output