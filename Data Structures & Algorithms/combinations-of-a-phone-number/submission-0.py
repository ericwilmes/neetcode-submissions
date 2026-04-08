class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        digit_to_letters = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def ite(i, running: str):
            if i == len(digits):
                if running:
                    output.append(running)
                return
            curr = digits[i]
            letters = digit_to_letters[curr]

            for l in letters:
                ite(i+1, running + l)

        ite(0, "")

        return output