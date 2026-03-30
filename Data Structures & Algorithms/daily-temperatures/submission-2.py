class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_i = stack[-1][1]
                output[stack_i] = i - stack_i
                stack.pop()
            stack.append((temp, i))
        return output