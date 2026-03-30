class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.search_m(matrix, target, 0, len(matrix)-1)
        if row == -1:
            return False
        return self.search(matrix[row], target, 0, len(matrix[row])-1)

    def search_m(self, matrix, target, l, r):
        # first find the row we should be in
        # then find the actual value

        if l > r:
            return -1

        m = (l + r) // 2
        if matrix[m][0] > target:
            return self.search_m(matrix, target, l, m-1)
        if matrix[m][-1] < target:
            return self.search_m(matrix, target, m+1, r)
        return m

    def search(self, matrix, target, l, r):
        # first find the row we should be in
        # then find the actual value

        if l > r:
            return False

        m = (l + r) // 2
        if matrix[m] > target:
            return self.search(matrix, target, l, m-1)
        if matrix[m] < target:
            return self.search(matrix, target, m+1, r)
        return True

