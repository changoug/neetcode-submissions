class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sec_freq, row_freq, col_freq = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if board[i][j] in row_freq[i]:
                    return False
                row_freq[i].add(board[i][j])

                if board[i][j] in col_freq[j]:
                    return False
                col_freq[j].add(board[i][j])

                if board[i][j] in sec_freq[(i // 3, j // 3)]:
                    return False
                sec_freq[(i // 3, j // 3)].add(board[i][j])
        return True
