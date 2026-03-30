class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, count in counts.items():
            freq[count].append(num)

        print(freq)
        output = []
        for i in range(len(freq) - 1, 0, -1):
            l = freq[i]
            for num in l:
                output.append(num)
                if len(output) == k:
                    return output