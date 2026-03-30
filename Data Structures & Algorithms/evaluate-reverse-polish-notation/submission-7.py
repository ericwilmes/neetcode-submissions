class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr_val = None
        for t in tokens:
            print(t)
            if is_number(t):
                stack.append(int(t))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                curr_val = eval(f"{val2}{t}{val1}")
                stack.append(int(curr_val))
        return stack[0]

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False