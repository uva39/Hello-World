import sys
f = sys.stdin.readline

def sol():
    n = int(f())
    mat = [[*map(int, f().split())] for _ in range(n)]
    visited = [False]*n
    minimum = int(1e5)

    def backtracking(depth, idx):
        nonlocal minimum
        if depth == n//2:
            score1, score2 = 0, 0
            for i in range(n):
                for j in range(n):
                    if visited[i] and visited[j]:
                        score1 += mat[i][j]
                    elif not visited[i] and not visited[j]:
                        score2 += mat[i][j]
            minimum = min(minimum, abs(score1 - score2))
            return

        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                backtracking(depth+1, i+1)
                visited[i] = False

    backtracking(0, 0)
    print(minimum)

if __name__ == '__main__':
    sol()