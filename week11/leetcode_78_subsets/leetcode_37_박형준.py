class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def get_col(board, col):
            tmp = []
            for row in range(9):
                tmp.append(board[row][col])
            return tmp

        def get_sub(board, row, col):
            sub_row = row // 3
            sub_col = col // 3
            tmp = []
            for i in range(sub_row * 3, (sub_row + 1) * 3):
                for j in range(sub_col * 3, (sub_col + 1) * 3):
                    tmp.append(board[i][j])
            return tmp

        def check_number(board, row, col, digit):
            board_row = board[row]
            board_col = get_col(board, col)
            board_sub = get_sub(board, row, col)
            if digit in board_row:
                return 0
            if digit in board_col:
                return 0
            if digit in board_sub:
                return 0
            return 1

        def finish_sudoku(board):
            tmp = sum(board, [])
            dot_cnt = tmp.count(".")
            if dot_cnt > 0:
                return 0
            return 1

        def next_idx(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        break
                if board[i][j] == ".":
                    break
            return i, j

        def solve(board, row, col):
            if board[row][col] != ".":
                return
            if finish_sudoku(board):
                return
            nums = [str(i) for i in range(1, 10)]
            for n in nums:
                if check_number(board, row, col, n):
                    board[row][col] = n
                    n_row, n_col = next_idx(board)
                    solve(board, n_row, n_col)
                    if finish_sudoku(board):
                        return
                    board[row][col] = "."

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    solve(board, row, col)
