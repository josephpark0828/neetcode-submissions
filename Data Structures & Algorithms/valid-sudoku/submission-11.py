class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:      
        seen_row = defaultdict(list)
        seen_col = defaultdict(list)
        seen_square = defaultdict(list)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in seen_row[r] or 
                   board[r][c] in seen_col[c] or
                   board[r][c] in seen_square[r // 3, c // 3]):
                   return False
                seen_row[r].append(board[r][c])
                seen_col[c].append(board[r][c])
                seen_square[r // 3, c // 3].append(board[r][c])
        
        return True