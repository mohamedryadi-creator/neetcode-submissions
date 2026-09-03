class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ligne=[]
        for i in range (9):
            for j in range (9):
                if board[i][j]!="." and board[i][j] in ligne:
                    return False
                if board[i][j]!="." and board[i][j] not in ligne:
                    ligne.append(board[i][j])
            ligne=[]
        colonne=[]
        for i in range (9):
            for j in range (9):
                if board[j][i]!="." and board[j][i] in colonne:
                    return False
                if board[j][i]!="." and board[j][i] not in colonne:
                    colonne.append(board[j][i])
            colonne=[]
        carre=[]
        for k in range(9):
            for i in range(3):
                for j in range (3):
                    r=(k//3)*3+i
                    c=(k%3)*3+j
                    if board[r][c]!=".":
                        if board[r][c] in carre:
                            return False
                        carre.append(board[r][c])
            carre=[]
        return True
