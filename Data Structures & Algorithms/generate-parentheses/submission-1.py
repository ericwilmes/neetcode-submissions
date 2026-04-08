class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def ite(curr, opens, closes):
            if opens <= 0 and closes <= 0:
                output.append(curr)

            # add an open
            if opens > 0:
                ite(curr + "(", opens-1, closes)

            # add a close
            if closes > 0 and opens != closes:
                ite(curr + ")", opens, closes-1)
                

        ite("(", n-1, n)

        return output