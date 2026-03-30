class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if stack:
                while stack and temp > stack[-1][0]:
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
            stack.append((temp, i))
        return output