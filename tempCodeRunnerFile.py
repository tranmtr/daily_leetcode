class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solve = False
        a = [1, 2, 3]
        def test():
            nonlocal solve
            solve = True
            a = [5, 6, 7]
        print(solve, a)