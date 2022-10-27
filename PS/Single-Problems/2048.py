# BOJ 12100 2048(easy)
import sys
input = sys.stdin.readline

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
def move_left():
    for i in range(n):
        for j in range(1, n):
            if board[i][j-1] == board[i][j]:
                board[i][j-1], board[i][j] = board[i][j]*2, 0
            while board[i][j-1] == 0:
                board[i][j-1], board[i][j] = board[i][j], 0
                j -= 1
def move_up():
    for i in range(1, n):
        for j in range(n):
            if board[i-1][j] == board[i][j]:
                board[i-1][j], board[i][j] = board[i][j]*2, 0
            while board[i-1][j] == 0:
                board[i-1][j], board[i][j] = board[i][j], 0
                i -= 1

move_left()
print(*board, sep='\n')