class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {(i, j): {} for i in range(3) for j in range(3)}
        rows = {i: {} for i in range(9)}
        cols = {i: {} for i in range(9)}

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == ".":
                    continue
                val = int(val)

                row = math.floor(i/3)
                col = math.floor(j/3)
                box = (row, col)

                print(i, j)

                print(box, row, col, val)

                if boxes[box].get(val) == 1 or rows[i].get(val) == 1 or cols[j].get(val) == 1:
                    print(boxes[box].get(val) == 1, rows[i].get(val) == 1, cols[j].get(val) == 1)
                    return False

                boxes[box][val] = boxes[box].get(val, 0) + 1
                rows[i][val] = rows[i].get(val, 0) + 1
                cols[j][val] = cols[j].get(val, 0) + 1

        return True