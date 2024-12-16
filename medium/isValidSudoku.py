class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)

        for i in range(n):
            checkLR = set()
            checkTB = set()
            checkCor = set()
            for k in range(n):
                if board[i][k] != '.':
                    if int(board[i][k]) in checkLR:
                        return False
                    else:
                        checkLR.add(int(board[i][k]))

                if board[k][i] != '.':
                    if int(board[k][i]) in checkTB:
                        return False
                    else:
                        checkTB.add(int(board[k][i]))

                kCor = int(k / 3) + int(int(i/3) * 3)
                iCor = int(k % 3) + int(int(i%3) * 3)

                if board[iCor][kCor] != '.':
                    if int(board[iCor][kCor]) in checkCor:
                        return False
                    else:
                        checkCor.add(int(board[iCor][kCor]))

        return True

def main():
    solution = Solution()
    print(solution.isValidSudoku(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".","2","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        ))

if __name__ == "__main__":
    main()   