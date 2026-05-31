class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            row = set()
            col = set()
            group = set()
            lst = []

            for j in range(len(board[i])):

                if board[i][j] != '.' and board[i][j] in row:
                    return False
                
                row.add(board[i][j])

                if board[j][i] != '.' and board[j][i] in col:
                    return False
                
                col.add(board[j][i])

                x = (i // 9) % 9 + j // 3
                y = (i * 3) % 9 + j % 3


                if board[x][y] != '.' and board[x][y] in group:
                    return False
                
                group.add(board[x][y])

        return True