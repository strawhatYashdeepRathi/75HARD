
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # for tracking the columns which already have a queen
        col = set()
        # This will hold the difference of row and col
        # This is required to identify diagonals
        # specifically for diagonals with increasing row and increasing col pattern
        # example: square (1,0) = 1-0 = 1
        # squares in same diagonals will have same difference
        # example: squares (0,0) and (8,8) are in the same diagonal
        # as both have same difference which is `0`
        diagpos = set()
        # This will hold the sum of row and col
        # This is required to identify antidiagonals.
        # specifically for diagonals with increasing row and decreasing col pattern
        # the squares in same diagonal won't have the same difference.
        # example: square (1,0) = 1-0 = 1
        # squares in same diagonals will have same difference
        # example: squares (0,7) and (1,6) are in the same diagonal
        # as both have same sum which is `7`
        diagneg = set()
        board = [["."]*n for i in range(n) ]   # start with empty board

        def backtrack(r):
            if r == n:
                copyx = ["".join(row) for row in board]
                res.append(copyx)
                return
            for c in range(n):
                if c in col or (r+c) in diagpos or (r-c) in diagneg:
                    continue
                col.add(c)
                diagpos.add(r+c)
                diagneg.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                diagneg.remove(r-c)
                diagpos.remove(r+c)
                board[r][c] = "."
        backtrack(0)
        return res



if __name__ == '__main__':
    n = 4
    obj = Solution()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print("Arrangement", i+1)
        for j in range(len(ans[0])):
            print(ans[i][j])
            print()